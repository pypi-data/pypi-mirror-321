import logging
import os
import pathlib

import dotenv
import sqlalchemy as sa
import typer
from openai import AzureOpenAI

from itsai.aspire import app
from itsai.aspire.vanna.base import VannaBase
from itsai.data_engine import utils
from itsai.data_engine.metadata import column

dotenv.load_dotenv()

_LOGGER = logging.getLogger(__name__)


def main(db: pathlib.Path = pathlib.Path('aspire.duckdb')) -> None:
    client = configure_agent(db)
    _train(client, db)


def configure_agent(db: pathlib.Path) -> app.App:
    client = AzureOpenAI()
    app_client = app.App(client, config=config)

    app_client.connect_to_duckdb(db.as_posix(), read_only=True)
    app_client.set_logger(_LOGGER)
    return app_client


config = {
    'model': 'gpt-4o',
    'azure_search_api_key': os.environ['AZURE_SEARCH_API_KEY'],
    'azure_search_endpoint': os.environ['AZURE_SEARCH_SERVICE_ENDPOINT'],
    'index_name': os.environ['AZURE_SEARCH_INDEX_NAME'],
}


def _train(vn: VannaBase, db: pathlib.Path) -> None:
    engine = sa.create_engine(
        f'duckdb:///{db.as_posix()}', connect_args={'read_only': True}
    )
    with engine.connect() as conn:
        _add_ddl(vn, conn)


# TODO: drop high-cardinality columns automatically
_EXCLUDE_COLUMNS = {'Indicator_Code', 'indicator_name', 'indicator_value'}


def _add_ddl(vn: VannaBase, conn: sa.Connection) -> None:
    df_information_schema = utils.result_as_frame(
        conn.execute(sa.text('SELECT * FROM INFORMATION_SCHEMA.COLUMNS'))
    )
    # TODO: for some reason, marks it as "the following columns..." in the extracted text
    df_table_schema = utils.result_as_frame(
        conn.execute(sa.text('SELECT * FROM INFORMATION_SCHEMA.TABLES'))
    )

    column_metadata = []
    for table in df_table_schema['table_name']:
        tbl = sa.table(table)
        m = column.generate_metadata(conn, tbl)
        column_metadata.extend(
            column.stringify(_m) for _m in m if _m.column.name not in (_EXCLUDE_COLUMNS)
        )

    ddl_objects = [
        df_table_schema,
        df_information_schema,
    ]
    # This will break up the information schema into bite-sized chunks that can be referenced by the LLM
    for ddl in ddl_objects:
        plan = vn.get_training_plan_generic(ddl)
        vn.train(plan=plan)

    for _column_metadata in column_metadata:
        vn.train(ddl=_column_metadata)


if __name__ == '__main__':
    logging.basicConfig(filename='tmp.log')
    typer.run(main)
