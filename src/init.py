#prepare dependency of this project

import os,sys
sys.path.append(os.path.abspath("."))

from utils import  Execmd
from ops import getOsType

os_constant_type_centos = {'centos','rhel','fedora'}
os_constant_type_u = {'ubuntu'}
os_constant_type_d = {'debian'}


local_os_type = getOsType()

if local_os_type  & os_constant_type_centos:
    Execmd("pip3 install sortedcontainers")