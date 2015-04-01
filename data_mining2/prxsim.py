# -*- coding: utf-8 -*-
#! /usr/bin/env python
from math import sqrt
# 皮尔逊相关度算法
def sim_pearson(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item]=1
    # 匹配person1和person2是否有共同之处，没有则返回
    if len(si)==0: return "两人没有共同爱好"
    # 得到列表个数
    n=len(si)
    # 对所有偏好求和
    sum1=sum([prefs[person1][item] for item in si])
    sum2=sum([prefs[person2][item] for item in si])
    # 求平方和
    sum1Sq=sum([pow(prefs[person1][item],2) for item in si])
    sum2Sq=sum([pow(prefs[person2][item],2) for item in si])
    # 求乘积之和
    pSum=sum([prefs[person1][item]*prefs[person2][item] for item in si])
    # 计算皮尔逊评价值
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r=num/den
    return r