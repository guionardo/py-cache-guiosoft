import os
import time
import unittest

from cache_gs import CacheGS
from cache_gs.cache_classes.file_cache import FileCache


class TestFileCache(unittest.TestCase):

    def setUp(self):
        cache_folder = 'path://.cache'
        if not os.path.isdir((cache_folder)):
            os.makedirs(cache_folder)

        self.file_cache = CacheGS(cache_folder)

    def test_purge(self):
        self.assertTrue(self.file_cache.set_value(
            'test', 'key', 'abcd', time.time()+1))
        time.sleep(1)
        self.assertTrue(self.file_cache.purge_expired() > 0)
