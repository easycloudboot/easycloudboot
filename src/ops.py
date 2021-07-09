import ipaddress
import sys
import os
sys.path.append(os.path.abspath("."))
from utils import getTmpl, Execmd

def setupDHCPService(networkName:str, dhcpSubnet: str,dhcpGateway: str):
    ips = ipaddress.IPv4Network(dhcpSubnet)
    mask = ips.netmask
    ipfrist,iplast = ips[0],ips[-1]
    gateway = ipaddress.ip_address(dhcpGateway)
    if gateway not in ips:
        raise Exception("wrong parameter:dhcpGateway address not in subnet")
    dhcpConfig = getTmpl("dhcp.conf.tmpl").format(network=networkName,subnet=ipfrist, first=iplast, last=iplast,gateway=dhcpGateway,netmask=mask)
    return  dhcpConfig

def getUplinkInfo(networkInterface:str):
    '''

    :param nicName: network interface name
    :return:
    '''
    Execmd("ethtool {intf}".format(intf=networkInterface)).get(raiseError=True)
    cmd = "timeout 60 tcpdump -nnnve -c 1 -i {intf}  ether proto 0x88cc 2>/dev/null".format(intf=networkInterface)
    return Execmd(cmd).get()

def getOsType():
    os = Execmd(
        "cat /etc/os-release | grep ID | grep -v VERSION | awk -F= '{print $2}' | sed 'N;s/\"//g;s/\\n/ /g'").get()
    osset = set(os.split(' '))
    return osset
