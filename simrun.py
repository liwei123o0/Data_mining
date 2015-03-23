# -*- coding: utf-8 -*-
#! /usr/bin/env python
import data
import ojsim
import prxsim
def simtop(person2):
    scores=[]
    for person1 in data.dicttostring:
        if person1 in person2:
            continue
        scores.append(ojsim.sim_distance\
                          (data.dicttostring,person1,person2))
    scores.sort()
    scores.reverse()
    print scores
if __name__=='__main__':
    # for other in data.dicttostring:
    #     print other
    simtop('刘浩')