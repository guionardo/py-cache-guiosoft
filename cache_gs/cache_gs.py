import os

from cache_gs.cache_classes.file_cache import FileCache
from cache_gs.cache_classes.redis_cache import RedisCache
from cache_gs.interfaces.super_cache import SuperCache


class CacheGS(SuperCache):

    def __init__(self, string_connection: str):
        if not isinstance(string_connection, str) or not string_connection:
            raise AttributeError('missing string_connection')
        self._cache: SuperCache = None
        if os.path.isdir(string_connection):
            self._cache = FileCache(string_connection)
        elif string_connection.startswith('redis:'):
            self._cache = RedisCache(string_connection)
        else:
            raise AttributeError('bad string_connection')

    def get_value(self, section: str, key: str, default=None) -> str:
        return self._cache.get_value(section, key, default)

    def set_value(self, section: str, key: str, value: str, expires_in: int = 0) -> bool:
        return self._cache.set_value(section, key, value, expires_in)

    def delete_value(self, section: str, key: str) -> bool:
        return self._cache.delete_value(section, key)

    def purge_expired(self):
        return self._cache.purge_expired()
