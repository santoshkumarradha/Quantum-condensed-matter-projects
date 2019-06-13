#!/usr/bin/env python3
from __future__ import print_function
from pymatgen.symmetry.bandstructure import HighSymmKpath as bnds
from pymatgen.io.vasp import Poscar
import subprocess, os, sys
import numpy as np
def runcmd(exe,opt=""):
        p = subprocess.Popen([exe, opt], stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out, err = p.communicate()
        return out.decode('utf-8'),err.decode('utf-8')
def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2:
            f2.write(string)
            f2.write(f.read())
    os.rename('newfile.txt',originalfile)
def syml_file(ctrl,kpts=30,syml_name="syml"):
    code="mpirun -np 1 lmchk --wsitep ctrl."+ctrl
    out,err=runcmd(code)
    insert("POSCAR","\n")
    poscar = Poscar.from_file("POSCAR")
    s= poscar.structure
    print("\n \n \n Your structure is : \n")
    print(s)
    path=bnds(s).get_kpoints(line_density=1, coords_are_cartesian=False)
    bz={}
    for i in range(len(path[0])):
        bz[path[1][i]]=path[0][i]
    np.set_printoptions(precision=5, suppress=True)
    f = open(syml_name+"."+ctrl, 'w')
    print("\n \n syml file - ")
    for i in range(len(bz)-1):
        kpt1=bz[list(bz.keys())[i]]
        kpt1_name=list(bz.keys())[i]
        kpt2=bz[list(bz.keys())[i+1]]
        kpt2_name=list(bz.keys())[i+1]
        kpt1=np.array2string(kpt1, formatter={'float_kind':lambda x: "%.4f" % x})
        kpt2=np.array2string(kpt2, formatter={'float_kind':lambda x: "%.4f" % x})
        print(kpts,"   ",str(kpt1).strip("[]"),"   ",str(kpt2).strip("[]"),"   ",kpt1_name,"  ",kpt2_name,file=f)
        print(kpts,"   ",str(kpt1).strip("[]"),"   ",str(kpt2).strip("[]"),"   ",kpt1_name,"  ",kpt2_name)
    print("\n Syml file generated as syml."+ctrl+"\n \n")


print("\n !!!!!!! Does not take in to consideration pos and site file !!!!! \n \n")
if len(sys.argv) > 1:
    ctrl=sys.argv[1]
    if os.path.isfile("ctrl."+ctrl):
        syml_file(ctrl)
    else:
        print("ctrl."+ctrl+" does not exist in this directory")
else:
    print("Please enter ctrl file and try again")
