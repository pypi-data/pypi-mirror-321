import glob
import json
import os
import pathlib
import pickle
import uuid
from abc import ABC, abstractmethod

import duckdb
import pandas as pd
import redis


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


class FSCache(Cache):
    def __init__(self, path: pathlib.Path = pathlib.Path('/tmp')):
        self._path = path

    def _filepath(self, id: str, field: str) -> pathlib.Path:
        return self._path.joinpath(f'{id}-{field}.pkl')

    def generate_id(self, *args, **kwargs):
        return str(uuid.uuid4())

    def set(self, id, field, value):
        with open(self._filepath(id, field), 'wb') as file:
            pickle.dump(value, file)

    def get(self, id, field):
        filepath = self._filepath(id, field)
        if not filepath.exists():
            return None
        with open(filepath, 'rb') as file:
            return pickle.load(file)

    def get_all(self, field_list) -> list:
        files = glob.glob(f'{self._path}*.pkl')
        ids = [file.split('-')[0] for file in files]
        return [
            {'id': id, **{field: self.get(id=id, field=field) for field in field_list}}
            for id in ids
        ]

    def delete(self, id):
        import glob

        for file in glob.glob(f'{self._path}/{id}-*'):
            os.remove(file)


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


class RedisCache(Cache):
    def __init__(self, host: str, port: int, password: str) -> None:
        self._client = redis.Redis(host=host, port=port, password=password, ssl=True)

    def generate_id(self, *args, **kwargs):
        return str(uuid.uuid4())

    def set(self, id, field, value):
        if field == 'df' and isinstance(value, pd.DataFrame):
            value.to_csv(f'{id}.csv', index=False)
            value = f'{id}.csv'

        data = self._client.get(id)
        if data:
            data = json.loads(data.decode())
        else:
            data = {}
        data[field] = value
        self._client.set(id, json.dumps(data))

    def get(self, id, field):
        data = self._client.get(id)
        if data:
            data = json.loads(data)
            value = data.get(field)
            if field == 'df' and value and value.endswith('.csv'):
                return pd.read_csv(value)
            return value
        return None

    def get_all(self, field_list) -> list:
        keys = self._client.keys()
        result = []
        for key in keys:
            data = json.loads(self._client.get(key))
            result.append(
                {'id': key.decode(), **{field: data.get(field) for field in field_list}}
            )
        return result

    def delete(self, id):
        self._client.delete(id)
