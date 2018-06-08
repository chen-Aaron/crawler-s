#-*- coding: utf-8 -*-
import requests

import urllib

import downLoad.index

import ConfigParser

import redis

from pyquery import PyQuery as pq

cf = ConfigParser.ConfigParser()

cf.read("db.ini")

rediser = {}

# rediser['host'] = cf.get("redis", "db_host")

# rediser['password'] = cf.get('redis', 'db_pass')

# rediser['port'] = cf.get('redis', 'db_port')

# r = redis.StrictRedis(host = rediser['host'], port = rediser['port'], password = rediser['password'])

url = 'http://18h.animezilla.com/manga'

res = requests.get(url);

html = pq(res.content);

print html('#main')

# r.lpush('tests', 'yes')



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
