import json
import pathlib
import uuid
from abc import ABC, abstractmethod

import duckdb
import pandas as pd


class Cache(ABC):
    """
    Define the interface for a cache that can be used to store data in a Flask app.
    """

    @abstractmethod
    def generate_id(self, *args, **kwargs):
        """
        Generate a unique ID for the cache.
        """
        pass

    @abstractmethod
    def get(self, id, field):
        """
        Get a value from the cache.
        """
        pass

    @abstractmethod
    def get_all(self, field_list) -> list:
        """
        Get all values from the cache.
        """
        pass

    @abstractmethod
    def set(self, id, field, value):
        """
        Set a value in the cache.
        """
        pass

    @abstractmethod
    def delete(self, id):
        """
        Delete a value from the cache.
        """
        pass


class MemoryCache(Cache):
    def __init__(self):
        self.cache = {}

    def _dump(self) -> None:
        pathlib.Path('tmp.json').write_text(json.dumps(self.cache, indent=4))

    def generate_id(self, *args, **kwargs):
        return str(uuid.uuid4())

    def set(self, id, field, value):
        if id not in self.cache:
            self.cache[id] = {}

        self.cache[id][field] = value

    def get(self, id, field):
        if id not in self.cache:
            return None

        if field not in self.cache[id]:
            return None

        return self.cache[id][field]

    def get_all(self, field_list) -> list:
        return [
            {'id': id, **{field: self.get(id=id, field=field) for field in field_list}}
            for id in self.cache
        ]

    def delete(self, id):
        if id in self.cache:
            del self.cache[id]


class DuckdbCache(Cache):
    def __init__(self, db_path: str | pathlib.Path = ':memory:'):
        self.conn = duckdb.connect(db_path)
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS cache (
                id TEXT PRIMARY KEY,
                data TEXT
            )
        """)

    def generate_id(self, *args, **kwargs):
        return str(uuid.uuid4())

    def set(self, id, field, value):
        # persist dataframes to disk, as we cannot store them in sqlite
        if field == 'df' and isinstance(value, pd.DataFrame):
            value.to_csv(f'{id}.csv', index=False)
            value = f'{id}.csv'

        cursor = self.conn.execute('SELECT data FROM cache WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            data = json.loads(row[0])
        else:
            data = {}
        data[field] = value
        self.conn.execute(
            'INSERT OR REPLACE INTO cache (id, data) VALUES (?, ?)',
            (id, json.dumps(data)),
        )

    def get(self, id, field):
        cursor = self.conn.execute('SELECT data FROM cache WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            data = json.loads(row[0])
            value = data.get(field)
            if field == 'df' and value and value.endswith('.csv'):
                return pd.read_csv(value)
            return value
        return None

    def get_all(self, field_list) -> list:
        cursor = self.conn.execute('SELECT id, data FROM cache')
        rows = cursor.fetchall()
        result = []
        for id, data in rows:
            data = json.loads(data)
            result.append(
                {'id': id, **{field: data.get(field) for field in field_list}}
            )
        return result

    def delete(self, id):
        self.conn.execute('DELETE FROM cache WHERE id = ?', (id,))
