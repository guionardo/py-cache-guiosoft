import time
import unittest

from cache_gs.cache_classes.file_cache import FileCache
from cache_gs import CacheGS


class TestFileCache(unittest.TestCase):

    def setUp(self):
        self.file_cache = CacheGS('.cache')

    def test_purge(self):
        self.assertTrue(self.file_cache.set_value(
            'test', 'key', 'abcd', time.time()+1))
        time.sleep(1)
        self.assertTrue(self.file_cache.purge_expired() > 0)
