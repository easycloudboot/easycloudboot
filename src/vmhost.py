from typing import List
import os,sys
sys.path.append(os.path.abspath("."))
from utils import  Execmd

class VmHost(object):
    def __init__(self):
        pass
    def provision(self):
        pass


class KvmHost(VmHost):
    def __init__(self):
        pass
    def provision(self):
        self.check()
        self.installpkgs()
        self.startupServices()

    def check(self):
        self.checkKvmModule()

    def installpkgs(self):
        pass

    def startupServices(self):
        pass

    def checkKvmModule(self):
        if not Execmd("lscpu | grep -o vmx").get(raiseError=True):
            raise Exception("cpu vmx not enabled")

        Execmd("lsmod | grep kvm || modprobe kvm ").get(raiseError=True)


#KvmHost().check()

