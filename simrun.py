# -*- coding: utf-8 -*-
#! /usr/bin/env python
import data
#欧几里德算法
import ojsim
#皮尔逊算法
import prxsim
#实现将相似度按最大值排序
def simtop(person2,sim):
    scores=[]
    for person1 in data.dicttostring:
        if person1 in person2:
            continue
        scores.append(sim(data.dicttostring,person1,person2))
    scores.sort()
    scores.reverse()
    print scores
#自定义使用相关算法与某人进行相似度计算，将排名前几位的打印出来
def topsim(perfs,person,n=5,sim=prxsim.sim_pearson):
    scores =[[sim(perfs,person,other),other]
                    for other in perfs if other!=person]
    #进行排序
    scores.sort()
    #反转
    scores.reverse()
    return scores[0:n]
#推荐未看过的电影并给出模拟评分
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
        #建立一个归一化列表
        for item,total in totals.items():
            print item,total
            print simsum[item]
            print total/simsum[item]
        rankings = [(total/simsum[item],item) for item,total in totals.items()]
        #返回经过排序的列表
        # print rankings
        rankings.sort()
        rankings.reverse()
        return rankings
#对调人员与物品推荐相关物品
def wptj(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})
            #物品和人员对调
            print result
            result[item][person]=person[person][item]
    return result

if __name__=='__main__':
    #第一种方法
    # simtop('刘浩',ojsim.sim_distance)
    #第二张方法
    # for i in topsim(data.dicttostring,'刘浩',n=3):
    #     print i
    #print getsim(data.dicttostring,'亚子')
    print wptj(data.dicttostring)