from src.ops import getDefaultIp

from unittest import TestCase
from unittest import mock

class TestOps(TestCase):
    def setUp(self):
       pass
    def test_GetDefaultIps(self):
        self.assertEqual(2, len(getDefaultIp()))