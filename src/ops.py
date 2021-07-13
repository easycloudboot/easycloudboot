import ipaddress
import sys
import os
sys.path.append(os.path.abspath(os.path.abspath(__file__) + "/../"))

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
        "cat /etc/os-release | egrep '^ID|ID_LIKE' | awk -F= '{print $2}' | sed 'N;s/\"//g;s/\\n/ /g'").get()
    osset = set(os.split(' '))
    return osset

def getDefaultIp():
    cmd = "ip a s | grep inet |grep -v inet6| grep -v '127.0.0.1' | head -1 | awk '{print $2,$NF}'"
    ipinfo =  Execmd(cmd).get(raiseError=True)
    if ipinfo.strip():
        return ipinfo.split(" ")
    raise Exception("ip address not found")