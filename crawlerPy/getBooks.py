#-*- coding: utf-8 -*-
import requests

import urllib

import downLoad.index

import page.index

import lists.index

import ConfigParser

import redis

import sys

from pyquery import PyQuery as pq

sys.getdefaultencoding()

cf = ConfigParser.ConfigParser()

cf.read("db.ini")

rediser = {}

# proxies = {'http': 'socks5:127.0.0.1:1086'}

rediser['host'] = cf.get("redis", "db_host")

rediser['password'] = cf.get('redis', 'db_pass')

rediser['port'] = cf.get('redis', 'db_port')

r = redis.StrictRedis(host = rediser['host'], port = rediser['port'], password = rediser['password'])

# url = 'http://18h.animezilla.com/manga'

# pages = page.index.Pages(url, r)

# pages.run()



# urls='http://18h.animezilla.com/manga/3209----[\xe4\xb8\xad\xe6\x96\x87H\xe6\xbc\xab][\xe5\xa5\xa5\xe6\xa3\xae\xe3\x83\x9b\xe3\x82\x99\xe3\x82\xa6\xe3\x82\xa4] \xe4\xbf\xba\xe5\xbe\x97\xe4\xbf\xae\xe5\xad\xa6\xe6\x97\x85\xe8\xa1\x8c/\xe6\x88\x91\xe7\x9a\x84\xe6\xa0\xa1\xe5\xa4\x96\xe6\x95\x99\xe5\xad\xb8\xe6\x97\x85\xe8\xa1\x8c [218P]'
# url = urls.split('----')
# url=url[0]
# url = url.split('/')
# print url[3]+url[4]

myUrl = r.lpop('manga')
# while myUrl:
#     print 'yes'

while myUrl:
    listCrawler = lists.index.List(myUrl, r) 

    listCrawler.run()
    
    myUrl = r.lpop('manga')


print 'finish'