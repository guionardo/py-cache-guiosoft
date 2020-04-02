from cache_gs.interfaces.super_cache import SuperCache
import os


class FileCache(SuperCache):

    def setup(self):
        self._string_connection = os.path.abspath(self._string_connection)
        if not os.path.isdir(self._string_connection):
            subpath = os.path.dirname(self._string_connection)
            if not os.path.isdir(subpath):
                raise FileNotFoundError(self._string_connection)
            self.log_info(
                'Creating cache folder [%s]', self._string_connection)
            os.makedirs(self._string_connection)

    def get_value(self, section, key, default=None):
        return super().get_value(section, key, default=default)

    def set_value(self, section, key, value, expires_in=0):
        return super().set_value(section, key, value, expires_in=expires_in)

    def purge_expired(self):
        return super().purge_expired()

    def _file_name(self, section: str, key: str, create_folder: bool):
        filename = self._section_key_hash(section, key)
        dirname = os.path.join(self._string_connection, filename[:2])
        if create_folder and not os.path.isdir(dirname):
            self.log_debug('Creating cache folder [%s]', dirname)
            os.makedirs(dirname)
        return os.path.join(dirname, filename)
