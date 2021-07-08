from subprocess import Popen,PIPE
from multiprocessing import  Process
import os,sys
sys.path.append(os.path.abspath("."))

def getTmpl(name):
    selfPath = os.path.abspath(__file__ + "/../../tmpl/" + name)
    print (selfPath)
    if not os.path.exists(selfPath): raise Exception("template file %s not exists" % name)
    with open(selfPath, 'r') as tmplFile:
        return tmplFile.read()

class Execmd(object):
    def __init__(self,cmd : str):
        self.cmd = cmd

    def get(self,raiseError=False) -> str:
        p = Popen(self.cmd, shell=True, stdout= PIPE, stderr = PIPE)
        stdout, stderr = p.communicate(timeout=2)

        if stderr and raiseError:
            raise Exception(stderr.decode(encoding='utf-8'))
        return stdout.decode(encoding='utf-8').strip()

    def fire(self):
        os.system(self.cmd)

    def asyncFire(self):
        p = Process(target=self.fire)
        p.start()
        return p.pid


if __name__ == '__main__':
    Execmd("curl http://www.baidu.com 2>&1 >/dev/null").asyncFire()
    print("output:" + Execmd("curl http:/dafadsxxxf.com").get())
    print(Execmd("curl http:/dafadsxxxf.com").get(raiseError=True))

