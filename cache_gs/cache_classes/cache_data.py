from datetime import datetime
from time import time


class CacheData:

    def __init__(self, section: str, key: str, value: str, expires_in: int, created: int = 0):
        section = '_' if not isinstance(
            section, str) or not section else section
        key = '_' if not isinstance(key, str) or not key else key
        value = str(value)
        expires_in = 0 if not isinstance(
            expires_in, int) or expires_in < 0 else expires_in

        self._section = section
        self._key = key
        self._value = value
        self._expires_in = expires_in
        if isinstance(created, datetime):
            self._created = created.timestamp()
        elif isinstance(created, int):
            self._created = created
        else:
            self._created = time()

    @property
    def section(self) -> str: return self._section

    @property
    def key(self) -> str: return self._key

    @property
    def value(self) -> str: return self._value

    @property
    def expires_in(self) -> int:
        """ Returns timestamp of expiration date (0 = never expires) """
        return self._expires_in

    @property
    def expired(self) -> bool: return time() > self._expires_in > 0
