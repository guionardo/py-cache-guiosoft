import datetime
import json
import os
import time
import unittest
from unittest.mock import Mock, patch

from cache_gs.cache_classes.cache_data_file import CacheData, CacheDataFile


class TestCacheDataFile(unittest.TestCase):

    def setUp(self):
        self.file_name = 'test.json'

    def tearDown(self):
        if os.path.isfile(self.file_name):
            os.unlink(self.file_name)

    def test_save(self):
        cd = CacheData("test_section", "test_key", "test_value", 0)
        cdf = CacheDataFile('test', cd)
        self.assertTrue(cdf.save(self.file_name))

        cdf2 = CacheDataFile(self.file_name)
        self.assertEqual(cdf.data, cdf2.data)

        cd2 = CacheData("test_section", "test_key",
                        "test_value_", 0, datetime.datetime.now())
        self.assertNotEqual(cd, cd2)

        self.assertNotEqual(cd, None)

    # @patch("json.dumps", Mock())
    # @patch("json.loads", Mock())
    # @patch("os.path.isfile", Mock())
    # def test_exceptions(self):
    #     json.dumps = lambda x: 1/0
    #     json.loads = lambda x: 1/0
    #     os.path.isfile.return_value = True
    #     cdf = CacheDataFile()
    #     self.assertFalse(cdf.load('test'))
    #     self.assertFalse(cdf.save('test'))
