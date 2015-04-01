# -*- coding: utf-8 -*-
#! /usr/bin/env python
from Data_mining.data_mining2 import prxsim
def readfile(filename):
    lines =[line for line in file(filename)]

    colnames=lines[0].strip().split('\t')[1:]
    rownames=[]
    data=[]
    for line in lines[1:]:
        p =line.strip().split('\t')
        rownames.append(p[0])
        data.append(float(x) for x in p[1:])
    return rownames,colnames,data
class bicluster:
    def __init__(self,vec,left=None,right=None,distance=0.0,id=None):
        self.left=left
        self.right=right
        self.vec=vec
        self.distance=distance