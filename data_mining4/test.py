# -*- coding: utf-8 -*-
#! /usr/bin/env python
import spider
#1.测试抓取网页URL
u'''
urllist =["http://bbs.ent.qq.com/forum.php"]
crawl =spider.spiders("")
crawl.spider(urllist)
'''
#2.测试数据库创建表和建立索引

# a =spider.spiders("scrapy.db")
# a.createindextables()

#3.为网页建立索引
# a =spider.spiders("scrapy.db")
# page =["https://pypi.python.org/pypi/pysqlite/2.6.3","http://bbs.ent.qq.com/forum.php"]
# a.spider(page)