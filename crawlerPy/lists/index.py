#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests

from pyquery import PyQuery as pq

class List:
    proxies = {'http': 'socks5:127.0.0.1:1086'}


    path = '#page-current'

    def __init__(self, url, redis):
        
        self.redis = redis

        url = url.split('----')

        self.url = url[0]

        urls = url[0]

        urls = urls.split('/')

        self.list = urls[3]+'list'

        self.row = urls[3] + urls[4]

        self.name = url[1]

        self.currentIndex = 1

    def run(self):

        self.saveList()

        self.manage()

    def manage(self):
        res = self.getLists()

        href = res.find('a:last-child').attr('href')

        href = href.split('/')

        self.currentIndex = self.currentIndex + 1

        if(href[5] == self.currentIndex):
            
            self.saveLink(res.find('#comic'))
            
            self.manage()

    # 获取图片
    def getLists(self):
        url = self.url + '/' + str(self.currentIndex)

        print url
               
        res = requests.get(url)

        html = pq(res.content)

        content = html(List.path)

        return content

    # 保存图片地址
    def saveLink(self, res):
        for i in res.items():
            self.redis.lpush(self.row, i.attr('src'))

    # 保存地址列表
    def saveList(self):
        self.redis.lpush(self.list, self.row + '---' + self.name)
