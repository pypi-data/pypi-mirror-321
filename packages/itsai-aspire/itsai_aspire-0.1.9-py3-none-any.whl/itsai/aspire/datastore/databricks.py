import os

from attr import dataclass
import dotenv
import pandas as pd
import sqlalchemy as sa

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
