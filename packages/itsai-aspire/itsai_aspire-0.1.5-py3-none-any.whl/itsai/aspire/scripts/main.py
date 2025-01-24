import logging
import os

import dotenv
import typer
from openai import AzureOpenAI

from itsai.aspire import app
from itsai.aspire.datastore import databricks
from itsai.aspire.vanna.flask import VannaFlaskApp

dotenv.load_dotenv()
_LOGGER = logging.getLogger(__name__)

_ACCESS_TOKEN = os.environ['DATABRICKS_TOKEN']
_SERVER_HOSTNAME = os.environ['DATABRICKS_SERVER_HOSTNAME']
_HTTP_PATH = os.environ['DATABRICKS_HTTP_PATH']


def main() -> None:
    client = configure_agent()
    app = VannaFlaskApp(
        client,
        summarization=False,
        suggested_questions=False,
        followup_questions=False,
        chart=False,
        allow_llm_to_see_data=True,
        title='mAiData',
        subtitle='Your data analyst for World Bank indicator data',
    )
    app.run()


def configure_agent() -> app.App:
    client = AzureOpenAI()
    app_client = app.App(client, config=config)
    _configure_sql_client(app_client)
    app_client.set_logger(_LOGGER)
    return app_client


def _configure_sql_client(app_client: app.App) -> None:
    sql_client = databricks.QueryExecutor(
        access_token=_ACCESS_TOKEN,
        server_hostname=_SERVER_HOSTNAME,
        http_path=_HTTP_PATH,
    )
    app_client.run_sql = sql_client
    app_client.run_sql_is_set = True
    app_client.dialect = 'PostgreSQL'
    # dummy query to crash the server if the sql client does not work
    sql_client('select 1')


config = {
    'model': os.environ['AZURE_OPENAI_MODEL'],
    'azure_search_api_key': os.environ['AZURE_SEARCH_API_KEY'],
    'azure_search_endpoint': os.environ['AZURE_SEARCH_SERVICE_ENDPOINT'],
    'index_name': os.environ['AZURE_SEARCH_INDEX_NAME'],
}


if __name__ == '__main__':
    logging.basicConfig(filename='tmp.log')
    typer.run(main)
