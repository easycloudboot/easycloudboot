import ipaddress
import sys
import os
sys.path.append(os.path.abspath(os.path.abspath(__file__) + "/../"))

from utils import getTmpl, Execmd

from enum import Enum

class LinuxServiceType(Enum):
    oneshot='oneshot'
    simple='simple'
    notify='notify'
    dbus='dbus'

def setupDHCPService(networkName:str, dhcpSubnet: str,dhcpGateway: str):
    ips = ipaddress.IPv4Network(dhcpSubnet)
    mask = ips.netmask
    ipfrist,iplast = ips[0],ips[-1]
    gateway = ipaddress.ip_address(dhcpGateway)
    if gateway not in ips:
        raise Exception("wrong parameter:dhcpGateway address not in subnet")
    dhcpConfig = getTmpl("dhcp.conf.tmpl").format(network=networkName,subnet=ipfrist, first=iplast, last=iplast,gateway=dhcpGateway,netmask=mask)
    return  dhcpConfig

def setupCustomStartupService(serviceName: str, cmd: str, type: LinuxServiceType, after='network.service', descripton = '',doc=''):
    serviceCfg = getTmpl("mysrv.service.tmpl").format(Cmd=cmd,Type=type.value,Descrption=serviceName,Doc=doc,After=after )
    with open('/usr/lib/systemd/system/%s.service' % serviceName , 'w') as srvFile:
        srvFile.write(serviceCfg)
    Execmd("systemctl enable %s" %serviceName).get()
    Execmd("systemctl start %s" % serviceName).get()
    return serviceCfg

