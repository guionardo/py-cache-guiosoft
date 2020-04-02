import logging
from hashlib import sha1


class SuperCache:
    LOGGER = logging.getLogger('cache_gs')

    def __init__(self, string_connection: str):
        if not isinstance(string_connection, str) or not string_connection:
            raise AttributeError(
                "bad string connection for {0}".format(type(self.__class__)))
        self._string_connection = string_connection
        self.setup()

    def setup(self):
        raise NotImplementedError

    def get_value(self, section: str, key: str, default=None) -> str:
        raise NotImplementedError

    def set_value(self, section: str, key: str, value: str, expires_in: int = 0) -> bool:
        raise NotImplementedError

    def delete_value(self, section: str, key: str) -> bool:
        raise NotImplementedError

    def purge_expired(self) -> int:
        raise NotImplementedError

    def _section_key_hash(self, section: str, key: str) -> str:
        sk = ("_" if not isinstance(section, str) or not section else section)+"." +\
            ("_" if not isinstance(key, str) or not key else key)
        hash = sha1(sk.encode('utf-8')).hexdigest()
        self.log_debug('HASH("%s", "%s") = %s', section, key, hash)
        return hash

    @classmethod
    def log_debug(cls, text, *args, **kwargs):
        cls.LOGGER.debug(text, *args, **kwargs)

    @classmethod
    def log_info(cls, text, *args, **kwargs):
        cls.LOGGER.info(text, *args, **kwargs)
