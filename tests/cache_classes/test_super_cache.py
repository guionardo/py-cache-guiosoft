import unittest
from unittest.mock import Mock, patch

from cache_gs.interfaces.super_cache import SuperCache


class TestSuperCache(unittest.TestCase):

    def test_init_no_string_connection(self):
        with self.assertRaises(AttributeError):
            SuperCache(None)

        with self.assertRaises(AttributeError):
            SuperCache('')

    def test_init_with_string_connection(self):
        with self.assertRaises(NotImplementedError):
            SuperCache('.cache')

