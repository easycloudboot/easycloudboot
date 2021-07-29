from typing import List
from enum import Enum

import os,sys
sys.path.append(os.path.abspath("../.."))
from src.commonutils import  Execmd
from src.linuxops.centos.utils import getDefaultIpv4

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

def setupLibvirtYum():
    appstream_repo='''
     [appstream]
    name=CentOS Linux $releasever - AppStream
    baseurl=http://mirrors.cloud.aliyuncs.com/$contentdir/$releasever/AppStream/$basearch/os/
    gpgcheck=0
    enabled=1
    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
     '''

    with open('/etc/yum.repos.d/appstream.repo','w') as appstreamFile:
        appstreamFile.write(appstream_repo)


def setUpLibvirtLogging():
    Execmd("virt-admin daemon-log-filters \"3:util 3:libvirt 3:storage 3:network 3:nodedev 3:qemu\"").get()
    Execmd("virt-admin daemon-log-outputs \"1:file:/var/log/libvirt/libvirtd.log\"").get()


def setupLibvirt():
    setupLibvirtYum()
    Execmd("yum install -y libvirt").get()
    setUpLibvirtLogging()


def setupQemu():

    Execmd("bash setupQemu.sh").get(raiseError=True)

class KvmHost(VmHost):
    def __init__(self):
        pass

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
            ip,itf = getDefaultIpv4()
            ret = Execmd("brctl create vmbridge && brctl addif vmbridge %s && ip addr add  %s dev vmbridge " % (itf, ip)).fire()
            return ret
