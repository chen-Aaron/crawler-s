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

proxies = {'http': 'socks5:127.0.0.1:1086'}

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

# myUrl = r.lpop('manga')

# listCrawler = lists.index.List(myUrl, r) 

# listCrawler.run()

# book = r.lpop('mangalist')

# book = book.split('---')

myli = r.llen('mangalist');

li = r.lrange('mangalist', 0, myli)

for i in li:
    withList = i.split('---')
    name = withList[1]
    listName = withList[0]
    length = r.llen(listName)
    imgList = r.lrange(listName, 0, myli)
    crawler = downLoad.index.Downloader(imgList, name)
    crawler.run()



# crawler = downLoad.index.Downloader(li)

# crawler.run()

# lists = lists.index.List('http://18h.animezilla.com/manga/3209----[\xe4\xb8\xad\xe6\x96\x87H\xe6\xbc\xab][\xe5\xa5\xa5\xe6\xa3\xae\xe3\x83\x9b\xe3\x82\x99\xe3\x82\xa6\xe3\x82\xa4] \xe4\xbf\xba\xe5\xbe\x97\xe4\xbf\xae\xe5\xad\xa6\xe6\x97\x85\xe8\xa1\x8c/\xe6\x88\x91\xe7\x9a\x84\xe6\xa0\xa1\xe5\xa4\x96\xe6\x95\x99\xe5\xad\xb8\xe6\x97\x85\xe8\xa1\x8c [218P]', r)

# pages.run()

# url = 'http://18h.animezilla.com/manga/313/1'

# res = requests.get(url, proxies=proxies);

# html = pq(res.content);

# content = html('#page-current')

# num = content.find('a:last-child').attr('href')
# num = num.split('/')
# print num[5]==str(2)
# content = res.content
# html = html('.entry-title')

# content = html('a')

# num=0

# for i in content.items():
#     num+=1;
#     print i.attr('href')
# print num
# with open('test.html', 'wb') as code:
#     code.write(content)
# r.lpush('mangas', [1,2,3])



# imgList = ['http://m.iprox.xyz/s/20180602/2070c0bf.jpg', 'http://m.iprox.xyz/s/20160523/0000-039d41.jpg']

# crawler = downLoad.index.Downloader(imgList)

# crawler.run()
# url = 'http://m.iprox.xyz/s/20180602/2070c0bf.jpg'

# headers = ({"Referer": "http://18h.animezilla.com/manga/608"})

# r = requests.get(url, headers=headers)

# fileName = url.split('/').pop()

# dirs = './imgs/'

# fileName = dirs + fileName 

# with open(fileName, 'wb') as code:
#     code.write(r.content)
