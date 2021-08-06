
class Fsm:
    #executing event can have 3 different state:
    # success/failed

    def __init__(self, name):
        self.name = name
        self.state = None

        self.state_trans_map = {
                                }

    def invoke(self,event,*args):
        if not self.state:
            return
        if (self.state,event) not in  self.state_trans_map:
            return
        try:
            getattr(self,event)(*args)
            self.state = self.state_trans_map[(self.state,event)]
        except:
            pass

class PhyMachine(Fsm):
    def __init__(self,name):
        super(PhyMachine,self).__init__(name)
        self.os = 'undefined'
        self.state = 'offline'
        self.state_trans_map = {('offline', 'clone'): 'online',
                                 ('online', 'offlineMachine'): 'offline',
                                 ('offline', 'removeMachine'): 'removed'

                                }

    def clone(self,os):
        self.os = os

    def offlineMachine(self):
        self.os = "undefined"

    def removeMachine(self,force):
        if not force:
            raise  Exception('fake except')


m = PhyMachine("machin1")
print(m.state,m.os)
m.invoke('clone','AliOS-7u2')
#m.clone("AliOS-7u2")

print(m.state,m.os)

m.invoke('clone','AliOS-7u3') # online+ clone not valid,so os won't change
print(m.state,m.os)

m.invoke('offline') #undefined event wont take effect
print(m.state,m.os)

m.invoke('offlineMachine')
print(m.state,m.os)

m.invoke("removeMachine","force")
print(m.state,m.os)

m.invoke("clone","debian")
print(m.state,m.os)






