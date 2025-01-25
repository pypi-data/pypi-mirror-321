import glob
import json
import os
import pathlib
import pickle
import uuid
from abc import ABC, abstractmethod


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
