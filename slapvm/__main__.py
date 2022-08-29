import os
from os import path
import sys
from slapvm.vm import SlapVM

if len(sys.argv) == 1:
    print('No path to executable program provided')
    exit(-1)

slapfile = path.join(os.getcwd(), str(sys.argv[-1:][0]))
if not path.exists(slapfile):
    print('{} does not exists'.format(slapfile))
    exit(-1)

with open(slapfile) as f:
    SlapVM.run(f.read())
