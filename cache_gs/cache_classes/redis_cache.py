from cache_gs.interfaces.super_cache import SuperCache

class RedisCache(SuperCache):

    def setup(self):
        return super().setup()

    def get_value(self, section, key, default=None):
        return super().get_value(section, key, default=default)

    def set_value(self, section, key, value, expires_in=0):
        return super().set_value(section, key, value, expires_in=expires_in)