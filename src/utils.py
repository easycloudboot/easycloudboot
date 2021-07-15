'''
This file implements basic utilites for linux host/vm ops.
'''

from subprocess import Popen,PIPE
from multiprocessing import  Process
import os,sys
sys.path.append(os.path.abspath("."))

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

def getTmpl(name):
    selfPath = os.path.abspath(__file__ + "/../../tmpl/" + name)
    print (selfPath)
    if not os.path.exists(selfPath): raise Exception("template file %s not exists" % name)
    with open(selfPath, 'r') as tmplFile:
        return tmplFile.read()

class Execmd(object):
    def __init__(self,cmd : str):
        self.cmd = cmd

    def get(self,raiseError=True) -> str:
        p = Popen(self.cmd, shell=True, stdout= PIPE, stderr = PIPE)
        stdout, stderr = p.communicate(timeout=2)

        if stderr and raiseError:
            raise Exception(stderr.decode(encoding='utf-8'))
        return stdout.decode(encoding='utf-8').strip()

    def fire(self):
        return os.system(self.cmd)

    def asyncFire(self):
        p = Process(target=self.fire)
        p.start()
        return p.pid


if __name__ == '__main__':
    Execmd("curl http://www.baidu.com 2>&1 >/dev/null").asyncFire()
    print("output:" + Execmd("curl http:/dafadsxxxf.com").get())
    print(Execmd("curl http:/dafadsxxxf.com").get(raiseError=True))

