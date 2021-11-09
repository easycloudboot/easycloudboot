from src.commonutils  import Execmd

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

def getDefaultIpv4():
    cmd = "ip a s | grep inet |grep -v inet6| grep -v '127.0.0.1' | head -1 | awk '{print $2,$NF}'"
    ipinfo =  Execmd(cmd).get(raiseError=True)
    if ipinfo.strip():
        return ipinfo.split(" ")
    raise Exception("ip address not found")

def isDiskSupportDisacrd():
    cmd = " cat /sys/block/{device}/queue/discard_granularity"
    return Execmd(cmd).get() != "0"

def getInterfaceUplinkInfo(nic):
    cmd = "timeout 60 tcpdump -nnnve -c 1 -i %s  ether proto 0x88cc" % nic
    return Execmd(cmd).get()

def getMostProcesses():
    cmd = "ps -eLf |awk '{print $10}'|sort | uniq -c | sort -nr |head"
    return Execmd(cmd).get()