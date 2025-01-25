import json
import uuid

import dotenv
import pandas as pd
import sqlalchemy as sa

from itsai.aspire.vanna.flask import _cache

dotenv.load_dotenv()


class QueryExecutor:
    def __init__(self, access_token: str, server_hostname: str, http_path: str) -> None:
        self._engine = sa.create_engine(
            url=f'databricks://token:{access_token}@{server_hostname}?'
            + f'http_path={http_path}'
        )

    def __call__(self, sql: str, **kwargs) -> pd.DataFrame:
        remapped = self._map_table_reference(sql)
        with self._engine.connect() as conn:
            df = pd.read_sql(remapped, conn)
        return df

    def _map_table_reference(self, sql: str) -> str:
        # TODO: remove hardcoded reference
        return sql.replace(
            'aspire.main.indicators', 'hive_metastore.imagebank.indicator'
        )


class DatabricksCache:
    def __init__(self, access_token: str, server_hostname: str, http_path: str) -> None:
        self._engine = sa.create_engine(
            url=f'databricks://token:{access_token}@{server_hostname}?'
            + f'http_path={http_path}'
        )

    def __call__(self, sql: str) -> pd.DataFrame:
        with self._engine.connect() as conn:
            res = conn.execute(sa.text(sql))
        return res


class DatabricksCacheClient(_cache.Cache):
    def __init__(self, client: DatabricksCache):
        self._client = client
        self._create_table()

    def _create_table(self):
        self._client("""
            CREATE TABLE IF NOT EXISTS qa_datascience_convaiqa.aspire.cache (
                id VARCHAR(255),
                data VARCHAR(320000),
                PRIMARY KEY (id)
            )
        """)

    def generate_id(self, *args, **kwargs):
        return str(uuid.uuid4())

    def set(self, id, field, value):
        if field == 'df' and isinstance(value, pd.DataFrame):
            value.to_csv(f'{id}.csv', index=False)
            value = f'{id}.csv'

        result = self._client(
            f"SELECT data FROM qa_datascience_convaiqa.aspire.cache WHERE id = '{id}'"
        )
        row = result.fetchone()
        if row:
            data = json.loads(row[0])
        else:
            data = {}
        data[field] = value
        self._client(
            f"INSERT OVERWRITE qa_datascience_convaiqa.aspire.cache VALUES ('{id}', '{json.dumps(data)}')"
        )

    def get(self, id, field):
        result = self._client(
            f"SELECT data FROM qa_datascience_convaiqa.aspire.cache WHERE id = '{id}'"
        )
        row = result.fetchone()
        if row:
            data = json.loads(row[0])
            value = data.get(field)
            if field == 'df' and value and value.endswith('.csv'):
                return pd.read_csv(value)
            return value
        return None

    def get_all(self, field_list) -> list:
        result = self._client(
            'SELECT id, data FROM qa_datascience_convaiqa.aspire.cache'
        )
        rows = result.fetchall()
        result_list = []
        for id, data in rows:
            data = json.loads(data)
            result_list.append(
                {'id': id, **{field: data.get(field) for field in field_list}}
            )
        return result_list

    def delete(self, id):
        self._client(
            f"DELETE FROM qa_datascience_convaiqa.aspire.cache WHERE id = '{id}'"
        )
