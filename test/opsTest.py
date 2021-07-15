from src.ops import setupCustomStartupService,LinuxServiceType
from src.utils import getDefaultIp
from unittest import TestCase
from unittest import mock

class TestOps(TestCase):
    def setUp(self):
       pass
    def test_GetDefaultIps(self):
        self.assertEqual(2, len(getDefaultIp()))

    def test_SetupCustomeService(self):
        cfg = setupCustomStartupService("myservice1","hostname",LinuxServiceType.oneshot)
        print(cfg)
