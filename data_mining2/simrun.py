# -*- coding: utf-8 -*-
#! /usr/bin/env python
from Data_mining.data_mining2 import ojsim, prxsim, data
#欧几里德算法
#皮尔逊算法
'''
函数方法说明：
1.simtopsimtop(person2,sim)
simtopsimtop指定某人与已知数据里其他人的相似度值
--preson2（必填） 某人姓名
--sim    （必填） 算法选择。 如：皮尔逊算法，欧几里德算法。
2.topsim(perfs,person,n=5,sim=prxsim.sim_pearson)
topsim指定某人与已知数据里其他人的相似度值前5名
--preson2（必填） 某人姓名
--sim    （必填） 算法选择。 如：皮尔逊算法，欧几里德算法。
--n       (可选)  默认前5名
3.getsim(prefs,person,sim=ojsim.sim_distance)
推荐未看过的电影并给出其他人对他的相似度评分
--prefs  （必填） 字典数据
--person （必填） 字典里包含的人名
--sim    （必填） 算法选择。 如：皮尔逊算法，欧几里德算法。
4.wptj(prefs)
对调人员与物品推荐相关物品（字典键值对调换）
--prefs  （必填） 字典数据
5.jywpbj(prefs,n=10)
构造物品比较数据集
--prefs  （必填） 字典数据
--n       (可选)  默认显示10个
'''

#1.实现将相似度按最大值排序
def simtop(person2,sim):
    scores=[]
    for person1 in data.dicttostring:
        if person1 in person2:
            continue
        scores.append(sim(data.dicttostring,person1,person2))
    scores.sort()
    scores.reverse()
    print scores
#2.自定义使用相关算法与某人进行相似度计算，将排名前几位的打印出来
def topsim(perfs,person,n=5,sim=prxsim.sim_pearson):
    scores =[[sim(perfs,person,other),other]
                    for other in perfs if other!=person]
    #进行排序
    scores.sort()
    #反转
    scores.reverse()
    return scores[0:n]
#3.推荐未看过的电影并给出模拟评分
def getsim(prefs,person,sim=ojsim.sim_distance):
    totals={}
    simsum={}
    for other in prefs:
        #不跟自己做比较
        if other in prefs[person]:continue
        #保存算法评价值
        simsf=sim(prefs,person,other)
        #排除评价值小于0的
        # print simsf
        if simsf <=0: continue
        for item in prefs[other]:
            #只对自己未看过的影片进行评价
            # print item
            if item not in prefs[person] or prefs[person][item]==0:
                # print item
                #相似度*评价值
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*simsf
                #相似度之和
                simsum.setdefault(item,0)
                simsum[item]+=simsf
        #建立一个归一化列表两种方式
        # for item,total in totals.items():
            # print item,total
            # print simsum[item]
            # print total/simsum[item]
        rankings = [(total/simsum[item],item) for item,total in totals.items()]
        #返回经过排序的列表
        # print rankings
        rankings.sort()
        rankings.reverse()
        return rankings
#4.对调人员与物品推荐相关物品
def wptj(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})
            result[item][person]=prefs[person][item]
    return result
#5.构造物品比较数据集
def jywpbj(prefs,n=10):
    #字典里存取以给出与这些物品最为相近的所有其他物品
    result={}
    #以物品为中心，对偏好矩阵事实倒置
    itemdd =wptj(prefs)
    # print itemdd
    c=0
    for item in itemdd:
        c+=1
        if c%100==0: print "数据构造进度：\n%d /%d"%(c,len(itemdd))
        #寻找最为相近的物品
        scores = topsim(itemdd,item,n=n,sim=prxsim.sim_pearson)
        # print scores
        result[item]=scores
    return result

if __name__=='__main__':
    #第一种方法
    # simtop('刘浩',ojsim.sim_distance)
    #第二张方法
    # for i in topsim(data.dicttostring,'刘浩',n=3):
    #     print i
    #第三个方法为某人推荐相关电影以及猜测评分
    #print getsim(data.dicttostring,'亚子')
    #第四个方法为某人推荐物品与某一电影最相近的影片
    #保存对调后的字典
    dict1= wptj(data.dicttostring)
    # print topsim(dict1,'Superman Returns',3)
    #第四个方法的变化应用和谁一起看推荐
    # print getsim(dict1,'Just My Luck')
    #第五个方法构造物品比较数据集
    print jywpbj(data.dicttostring)
    # for name in jywpbj(data.dicttostring)['Superman Returns']:
    #     print name