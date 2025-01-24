"""Fork of Vanna azure aisearch module.

had to implement a custom class as we want to use openai embedding."""

import ast
import json
import os

import pandas as pd
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    ExhaustiveKnnAlgorithmConfiguration,
    ExhaustiveKnnParameters,
    SearchableField,
    SearchField,
    SearchFieldDataType,
    SearchIndex,
    VectorSearch,
    VectorSearchAlgorithmKind,
    VectorSearchAlgorithmMetric,
    VectorSearchProfile,
)
from azure.search.documents.models import VectorFilterMode, VectorizedQuery
from langchain_openai import AzureOpenAIEmbeddings

from itsai.aspire.vanna.base import VannaBase
from itsai.aspire.vanna.utils import deterministic_uuid


class AzureAISearch(VannaBase):
    """
    AzureAISearch_VectorStore is a class that provides a vector store for Azure AI Search.

    Parameters
    -----------
        config (dict): Configuration dictionary. Defaults to {}. You must provide an API key in the config.
        -   azure_search_endpoint (str, optional): Azure Search endpoint. Defaults to `os.environ['AZURE_SEARCH_ENDPOINT']`.
        -   azure_search_api_key (str): Azure Search API key.
        -   dimensions (int, optional): Dimensions of the embeddings. Defaults to 1536 for text-embedding-3
        -   index_name (str, optional): Name of the index. Defaults to "vanna-index".
        -   n_results (int, optional): Number of results to return. Defaults to 10.
        -   n_results_ddl (int, optional): Number of results to return for DDL queries. Defaults to the value of n_results.
        -   n_results_sql (int, optional): Number of results to return for SQL queries. Defaults to the value of n_results.
        -   n_results_documentation (int, optional): Number of results to return for documentation queries. Defaults to the value of n_results.

    Raises
    ------
        ValueError: If config is None, or if 'azure_search_api_key' is not provided in the config.
    """

    def __init__(self, config=None):
        VannaBase.__init__(self, config=config)

        self.config = config or None

        if config is None:
            raise ValueError(
                "config is required, pass an API key, 'azure_search_api_key', in the config."
            )

        self.dimensions = config.get('dimensions', 1536)
        azure_search_endpoint = config.get(
            'azure_search_endpoint', os.environ['AZURE_SEARCH_ENDPOINT']
        )
        azure_search_api_key = config.get('azure_search_api_key')

        self.index_name = config.get('index_name', 'dummy-index')
        self.n_results_ddl = config.get('n_results_ddl', config.get('n_results', 10))
        self.n_results_sql = config.get('n_results_sql', config.get('n_results', 10))
        self.n_results_documentation = config.get(
            'n_results_documentation', config.get('n_results', 10)
        )

        if not azure_search_api_key:
            raise ValueError(
                "'azure_search_api_key' is required in config to use AzureAISearch_VectorStore"
            )

        self.index_client = SearchIndexClient(
            endpoint=azure_search_endpoint,
            credential=AzureKeyCredential(azure_search_api_key),
        )
        self._embedder = AzureOpenAIEmbeddings(
            model=config.get('embedding_model', 'text-embedding-3-small')
        )

        self.search_client = SearchClient(
            endpoint=azure_search_endpoint,
            index_name=self.index_name,
            credential=AzureKeyCredential(azure_search_api_key),
        )

        if self.index_name not in self._get_indexes():
            self._create_index()

    def _create_index(self) -> None:
        result = _create_index(self.index_client, self.dimensions, self.index_name)
        print(f'{result.name} created')

    def _get_indexes(self) -> list[str]:
        return [index for index in self.index_client.list_index_names()]

    def add_ddl(self, ddl: str, **kwargs) -> str:
        id = deterministic_uuid(ddl) + '-ddl'
        document = {
            'id': id,
            'document': ddl,
            'type': 'ddl',
            'document_vector': self.generate_embedding(ddl, **kwargs),
        }
        self.search_client.upload_documents(documents=[document])
        return id

    def add_documentation(self, doc: str, **kwargs) -> str:
        id = deterministic_uuid(doc) + '-doc'
        document = {
            'id': id,
            'document': doc,
            'type': 'doc',
            'document_vector': self.generate_embedding(doc, **kwargs),
        }
        self.search_client.upload_documents(documents=[document])
        return id

    def add_question_sql(self, question: str, sql: str, **kwargs) -> str:
        question_sql_json = json.dumps(
            {'question': question, 'sql': sql}, ensure_ascii=False
        )
        id = deterministic_uuid(question_sql_json) + '-sql'
        document = {
            'id': id,
            'document': question_sql_json,
            'type': 'sql',
            'document_vector': self.generate_embedding(question_sql_json, **kwargs),
        }
        self.search_client.upload_documents(documents=[document])
        return id

    def get_related_ddl(self, text: str, **kwargs) -> list[str]:
        result = []
        vector_query = VectorizedQuery(
            vector=self.generate_embedding(text, **kwargs), fields='document_vector'
        )
        df = pd.DataFrame(
            self.search_client.search(
                top=self.n_results_ddl,
                vector_queries=[vector_query],
                select=['id', 'document', 'type'],
                filter=f"type eq 'ddl'",
            )
        )

        if len(df):
            result = df['document'].tolist()
        return result

    def get_related_documentation(self, text: str, **kwargs) -> list[str]:
        result = []
        vector_query = VectorizedQuery(
            vector=self.generate_embedding(text, **kwargs), fields='document_vector'
        )

        df = pd.DataFrame(
            self.search_client.search(
                top=self.n_results_documentation,
                vector_queries=[vector_query],
                select=['id', 'document', 'type'],
                filter=f"type eq 'doc'",
                vector_filter_mode=VectorFilterMode.PRE_FILTER,
            )
        )

        if len(df):
            result = df['document'].tolist()
        return result

    def get_similar_question_sql(self, question: str, **kwargs) -> list[str]:
        result = []
        # Vectorize the text
        vector_query = VectorizedQuery(
            vector=self.generate_embedding(question, **kwargs), fields='document_vector'
        )
        df = pd.DataFrame(
            self.search_client.search(
                top=self.n_results_sql,
                vector_queries=[vector_query],
                select=['id', 'document', 'type'],
                filter=f"type eq 'sql'",
            )
        )

        if len(df):  # Check if there is similar query and the result is not empty
            result = [ast.literal_eval(element) for element in df['document'].tolist()]

        return result

    def get_training_data(self, **kwargs) -> list[str]:
        search = self.search_client.search(
            search_text='*',
            select=['id', 'document', 'type'],
            filter="(type eq 'sql') or (type eq 'ddl') or (type eq 'doc')",
        ).by_page()

        df = pd.DataFrame([item for page in search for item in page])

        if len(df):
            df.loc[df['type'] == 'sql', 'question'] = df.loc[df['type'] == 'sql'][
                'document'
            ].apply(lambda x: json.loads(x)['question'])
            df.loc[df['type'] == 'sql', 'content'] = df.loc[df['type'] == 'sql'][
                'document'
            ].apply(lambda x: json.loads(x)['sql'])
            df.loc[df['type'] != 'sql', 'content'] = df.loc[df['type'] != 'sql'][
                'document'
            ]

            return df[['id', 'question', 'content', 'type']]

        return pd.DataFrame()

    def remove_training_data(self, id: str, **kwargs) -> bool:
        result = self.search_client.delete_documents(documents=[{'id': id}])
        return result[0].succeeded

    def remove_index(self, **kwargs):
        self.index_client.delete_index(self.index_name)

    def generate_embedding(self, data: str, **kwargs) -> list[float]:
        return self._embedder.embed_query(data, **kwargs)


def _create_index(client: SearchIndexClient, dimensions: int, name: str) -> SearchIndex:
    fields = [
        SearchableField(
            name='id', type=SearchFieldDataType.String, key=True, filterable=True
        ),
        SearchableField(
            name='document',
            type=SearchFieldDataType.String,
            searchable=True,
            filterable=True,
        ),
        SearchField(
            name='type',
            type=SearchFieldDataType.String,
            filterable=True,
            searchable=True,
        ),
        SearchField(
            name='document_vector',
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=dimensions,
            vector_search_profile_name='ExhaustiveKnnProfile',
        ),
    ]

    vector_search = VectorSearch(
        algorithms=[
            ExhaustiveKnnAlgorithmConfiguration(
                name='ExhaustiveKnn',
                kind=VectorSearchAlgorithmKind.EXHAUSTIVE_KNN,
                parameters=ExhaustiveKnnParameters(
                    metric=VectorSearchAlgorithmMetric.COSINE
                ),
            )
        ],
        profiles=[
            VectorSearchProfile(
                name='ExhaustiveKnnProfile',
                algorithm_configuration_name='ExhaustiveKnn',
            )
        ],
    )

    index = SearchIndex(name=name, fields=fields, vector_search=vector_search)
    result = client.create_or_update_index(index)
    return result
