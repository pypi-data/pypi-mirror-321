import json
import pathlib
import uuid
from abc import ABC, abstractmethod

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


class RedisCache(Cache):
    def __init__(self, host: str, port: int, password: str):
        self._client = redis.Redis(host=host, port=port, password=password, ssl=True)

    def generate_id(self, *args, **kwargs):
        return str(uuid.uuid4())

    def set(self, id, field, value):
        self._client.set(_key(id, field), _serialize(value), ex=1800)

    def get(self, id, field):
        obj = self._client.get(_key(id, field))
        return deserialize(obj)

    def get_all(self, field_list) -> list:
        # not implemented
        return []

    def delete(self, id):
        pattern = f'{id}:*'
        for key in self._client.scan_iter(match=pattern):
            self._client.delete(key)


def _key(id: str, field: str) -> str:
    return f'{id}-{field}'


def _serialize(obj):
    if isinstance(obj, pd.DataFrame):
        return json.dumps(obj.to_dict('records'))
    return obj


def deserialize(obj):
    try:
        parse = pd.DataFrame.from_records(json.loads(obj.decode()))
        return parse
    except Exception:
        return obj.decode()
