# -*- coding: utf-8 -*-
#! /usr/bin/env python
import simrun
def loadData(path='E:/ml-100k'):
    #获取影片标题
    data={}
    for line in open(path+'/u.item'):
        (id,title)=line.split('|')[0:2]
        data[id]=title
        # print data
    #加载数据
    prefs={}
    for line in open(path+'/u.data'):
        (user,movieid,rating,ts)=line.split('\t')
        prefs.setdefault(user,{})
        # print user,movieid,rating,ts
        prefs[user][data[movieid]]=float(rating)
    # print prefs
    return prefs
a=loadData()
print a
print simrun.getsim(a,'87')[0:50]