# -*- coding: utf-8 -*-
#! /usr/bin/env python
import data
from pydelicious import get_popular,get_userposts,get_urlposts
a= get_popular(tag='programming')
for i in a:
    print get_urlposts(i)
def initializeUserDict(tag,count=5):
    user_dict={}
    #获取前count个最受欢迎的连接张贴记录
    for p1 in get_popular(tag=tag)[0:count]:
        for p2 in get_urlposts(p1['href']):
            user=p2['user']
            user_dict[user]={}
    print user_dict
    return user_dict
# initializeUserDict(tag='programming')