from vmspec import GenericSpec
import os
from commonutils import  Execmd
from  jinja2 import Template

class KvmBooter:
    def __init__(self,id: str,spec: GenericSpec):
        self.spec = spec
        self.id = id


    #Todo: use cloud-init to inject other configurations
    def boot(self):
        qemu_kvm_template = open(os.path.abspath(__file__ + "/../../../tmpl/qemu_kvm.conf.tmpl"), 'r').read()
        kvm_xml_template = Template(qemu_kvm_template).render(self.spec.toDict())
        with open("%s.xml" % self.id,"w") as define_xml:
            define_xml.write(kvm_xml_template)
            define_xml.flush()
            Execmd("virsh define {xml} && virsh start {domain}".format(xml=define_xml,domain=self.id))
