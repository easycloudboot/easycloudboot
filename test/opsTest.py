from src.linuxops.centos.ops import setupCustomStartupService,LinuxServiceType
from src.linuxops.centos.utils import getDefaultIpv4
from unittest import TestCase


class TestOps(TestCase):
    def setUp(self):
       pass
    def test_GetDefaultIps(self):
        self.assertEqual(2, len(getDefaultIpv4()))

    def test_SetupCustomeService(self):
        cfg = setupCustomStartupService("myservice1","hostname",LinuxServiceType.oneshot)
        print(cfg)
