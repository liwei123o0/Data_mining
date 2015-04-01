# -*- coding: utf-8 -*-
#! /usr/bin/env python
# 欧几里德算法，返回person1与person2基于距离的相似度评分
def sim_distance(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item]=1
    # 匹配person1和person2是否有共同之处，没有则返回
    if len(si)==0: return "两人没有共同爱好"
    # 计算person1和person2所有共同爱好评分差值的平方和
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                      for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_of_squares)
