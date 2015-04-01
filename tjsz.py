# -*- coding: utf-8 -*-
#! /usr/bin/env python
import simrun
import time
import data
#基于用户的推荐
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
#基于物品的推荐
def getwupintj(prefs,itemMatch,user):
    userRatings=prefs[user]
    scores={}
    totalSim={}
    #循环遍历由当前用户评分的商品
    for(item,rating) in userRatings.items():
        #循环遍历与当前用户评分的物品
        for (sim,item2) in itemMatch[item]:
            #如果该用户已经对当前物品做过评价，则将其忽略
            if item2 in userRatings:continue
            #评价值与相似度加权之和
            scores.setdefault(item2,0)
            scores[item2]+=sim * rating
        #将每个合计值除以加权和，求出平均值
        rankings = [(scores/totalSim[item],item) for item,scores in scores.items()]
        #按最高到最低排序，返回评分结果
        rankings.sort()
        rankings.reverse()
        return rankings

prefs=loadData()
#1.基于用户的推荐方式
# print simrun.getsim(prefs,'2')[0:3]
#2.基于物品的推荐方式
# itemwupin = simrun.jywpbj(prefs,n=50)
# print getwupintj(prefs,itemwupin,'87')
#3.测试getwupintj方法
itemwupin = simrun.jywpbj(data.dicttostring,n=10)
print getwupintj(data.dicttostring,itemwupin,'李伟')