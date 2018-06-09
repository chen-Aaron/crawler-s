#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests

from pyquery import PyQuery as pq

class Pages:
    
    path = '.pure-u-1-2 .entry-title a'

    proxies = {'http': 'socks5:127.0.0.1:1086'}

    def __init__(self, pageUrl, redis):
       
       self.currentIndex = 1

       urls = pageUrl.split('/')

       self.row = urls[3]

       self.redis = redis

       self.myUrl = pageUrl

       self.pageUrl = pageUrl + '/page/'

    # 主入口
    def run(self):
        res = self.getBooks()

        if(res.html() != None):
            
            self.saveLink(res)

            self.currentIndex = self.currentIndex + 1
            
            self.run()


    # 获取图片链接地址
    def getBooks(self):
        url = ''

        if(self.currentIndex == 1):
           url = self.myUrl
        else:
           url = self.pageUrl + str(self.currentIndex)
               
        res = requests.get(url)

        print url

        html = pq(res.content)

        content = html(Pages.path)

        return content

    # 将图片保存至reids队列
    def saveLink(self, res):
        for i in res.items():
            text = i.text().replace(' ', '')
            self.redis.lpush(self.row, i.attr('href')+'----'+text)



       


