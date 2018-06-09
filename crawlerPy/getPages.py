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

url = 'http://18h.animezilla.com/manga'

pages = page.index.Pages(url, r)

pages.run()