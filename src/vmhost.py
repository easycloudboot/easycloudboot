from typing import List
from enum import Enum


import os,sys
sys.path.append(os.path.abspath("."))
from utils import  Execmd,getDefaultIp

class VMHostNetwork(Enum):
    Bridge=1
    SRIOV=2

class CPUARCH(Enum):
    AARCH64 = 1
    X86_64 = 2

class VmHost(object):
    def __init__(self):
        pass
    def provision(self):
        pass


def setupLibvirt():
    Execmd("bash setupLibvirt.sh").get(raiseError=True)


def setupQemu():

    Execmd("bash setupQemu.sh").get(raiseError=True)

class KvmHost(VmHost):
    def __init__(self):
        pass

    def init

    def provision(self):
        self.check()
        self.setupDependencies()
        self.startupServices()


    def check(self):
        self.checkKvmModule()

    def setupDependencies(self):
        '''
        install libvirt and qemu packages
        :return:
        '''
        setupQemu()
        setupLibvirt()
        pass

    def startupServices(self):
        Execmd("systemctl enable libvirtd && systemctl start libvirtd ").get(raiseError=True)


    def checkKvmModule(self):
        if not Execmd("lscpu | grep -o vmx").get(raiseError=True):
            raise Exception("cpu vmx not enabled")

        Execmd("lsmod | grep kvm || modprobe kvm ").get(raiseError=True)

    def setupNetwork(self,networkType=VMHostNetwork.Bridge):
        '''
        setup bridge network if kvm need to connectable to host network
        :param networkType:
        :return:
        '''
        if networkType == VMHostNetwork.Bridge:
            ip,itf = getDefaultIp()
            ret = Execmd("brctl create vmbridge && brctl addif vmbridge %s && ip addr add  %s dev vmbridge " % (itf, ip)).fire()
            return ret
