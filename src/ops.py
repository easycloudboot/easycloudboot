import ipaddress
import sys
import os
sys.path.append(os.path.abspath("."))
from utils import getTmpl

def setupDHCPService(networkName:str, dhcpSubnet: str,dhcpGateway: str):
    ips = ipaddress.IPv4Network(dhcpSubnet)
    mask = ips.netmask
    ipfrist,iplast = ips[0],ips[-1]
    gateway = ipaddress.ip_address(dhcpGateway)
    if gateway not in ips:
        raise Exception("wrong parameter:dhcpGateway address not in subnet")
    dhcpConfig = getTmpl("dhcp.conf.tmpl").format(network=networkName,subnet=ipfrist, first=iplast, last=iplast,gateway=dhcpGateway,netmask=mask)
    return  dhcpConfig

print(setupDHCPService('netowrk1','10.0.0.0/24','10.0.0.100'))