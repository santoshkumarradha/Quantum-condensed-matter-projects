#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Code detailes
   Code created by Santosh Kumar Radha (Santosh).
   updated last on 06/13/2017
   contact me at srr70@case.edu for any updates or any information about the code.


   If I have left the university, my webpage can be found at
   www.santoshkumarradha.me
"""




from __future__ import print_function
from pymatgen.symmetry.bandstructure import HighSymmKpath as bnds
from pymatgen.io.vasp import Poscar
import subprocess, os, sys
import argparse
import numpy as np
from seekpath import *
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
def syml_file(ctrl,kpts=30,syml_name="syml",rpos=None):
    code="mpirun -np 1 lmchk --wsitep ctrl."+ctrl
    out,err=runcmd(code)
    insert("POSCAR","\n")
    poscar = Poscar.from_file("POSCAR")
    s= poscar.structure

    struc=(np.ndarray.tolist(s.lattice.matrix),np.ndarray.tolist(s.frac_coords),list(s.atomic_numbers))
    t=get_path(struc)
    print("\nCrystal Information : \n")
    print(s)
    print("\nSpace group              : ",t['spacegroup_number'])
    print("spacegroup international : ",t['spacegroup_international'])
    print("bravais lattice          : ",t['bravais_lattice'])

    np.set_printoptions(precision=5, suppress=True)
    f = open(syml_name+"."+ctrl, 'w')
    print("\n \nGenerated syml file - \n")
    for i in t["path"]:
        kpt1=t["point_coords"][i[0]]
        kpt1_name=i[0]
        kpt2=t["point_coords"][i[1]]
        kpt2_name=i[1]
        if kpt1_name=="GAMMA":
            kpt1_name="\Gamma"
        if kpt2_name=="GAMMA":
            kpt2_name="\Gamma"
        kpt1=np.array2string(np.array(kpt1), formatter={'float_kind':lambda x: "%.4f" % x})
        kpt2=np.array2string(np.array(kpt2), formatter={'float_kind':lambda x: "%.4f" % x})
        print(kpts,"   ",str(kpt1).strip("[]"),"   ",str(kpt2).strip("[]"),"   ",kpt1_name," to ",kpt2_name,file=f)
        print(kpts,"   ",str(kpt1).strip("[]"),"   ",str(kpt2).strip("[]"),"   ",kpt1_name," to ",kpt2_name)

    print("\nSyml file generated as "+syml_name+"."+ctrl+"\n \n")






parser = argparse.ArgumentParser(description='Genertates Syml file for a given ctrl')
parser.add_argument("-c",
    '--ctrl',
    default="temp",
    help='ctrl file name (default: temp)',
    required=True
)
parser.add_argument("-rpos",
    '--rpos',
    default=None,
    help='pos file, if it exists (default: None)'
)
parser.add_argument("-kpts",
    '--kpts',
    default=30,
    help='num of kpts (default: 30)'
)
parser.add_argument("-symlfile",
    '--symlfile',
    default="syml",
    help='num of kpts (default: syml)'
)
inputs = parser.parse_args()
if os.path.isfile("ctrl."+inputs.ctrl):
        syml_file(ctrl=inputs.ctrl,rpos=inputs.rpos,kpts=inputs.kpts,syml_name=inputs.symlfile)
else:
        print("ctrl."+inputs.ctrl+" does not exist in this directory try again")
