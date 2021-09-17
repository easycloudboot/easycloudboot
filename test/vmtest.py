from vmspec import Disk,GenericSpec
import os

qemu_kvm_template = open(os.path.abspath(__file__ + "/../../tmpl/qemu_kvm.conf.tmpl" ),'r').read()
disks = [Disk(device="sda",size="500",ssd=True, file="/store/sda.qcow2"),Disk(device="sdb",size="500",ssd=True, file="/store/sdb.qcow2")]
spec = GenericSpec(vcpu=32,memory=64,disks=disks)
