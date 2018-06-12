#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

import urllib

import os

class Downloader:
    
    files = {
        "num": 608,
        "name": "123" 
    }
    dirs = '../imgs/'

    headers = {"Referer": "http://18h.animezilla.com/manga/608"}

    def __init__(self, imgList, name):
        self.files = {"num": 608, "name": "123"}
        self.list = imgList
        self.book = name
        self.dir = Downloader.dirs + self.book

        if(not self.isDirExit(self.dir)):
            self.makdeDir(self.dir)

    def run(self):
       
        length = len(self.list)
        for i in range(0, length):
            res = self.download(self.list[i])
            fileName = self.getFileName(self.list[i])
            self.saveFile(res, fileName)

    def isDirExit(self, dir):
        result = os.path.exists(dir)
        print result
        return result

    def makdeDir(self, dir):
        os.makedirs(dir)
        # self.run()
    
    # 下载图片
    def download(self, url):
        content = requests.get(url, headers= Downloader.headers)

        return content
    
    def saveFile(self, Res, fileName):
        print fileName
        with open(fileName, 'wb') as code:
            code.write(Res.content)

    def getFileName(self, url):
        fileName = url.split('/').pop()
        fileName = fileName.split('.').pop()
        nums = self.getNums()
        fileName = str(nums) + '.' + fileName
        fileName = self.dir + '/' + fileName
        return fileName

    def getNums(self):
        length = 1
        for root, dirs, files in os.walk(self.dir, topdown=False):
            length = len(files)
        return length
        
