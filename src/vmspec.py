from pydantic import BaseModel
from typing import  List

class Disk(BaseModel):
    device: str
    size: int  #size with G
    ssd: bool #is ssd or not
    file: str

class GenericSpec(BaseModel):
    vcpu: int
    memory: int # 4C32G
    disks: List[Disk]
    def toDict(self):
        return {"vcpu": self.vcpu, "memory": self.memory * 1024 * 1024, "disks": disks}





