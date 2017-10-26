#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
from bs4 import  BeautifulSoup

response = requests.get("http://www.autohome.com.cn/news/")
response.encoding='gbk'
soup = BeautifulSoup(response.text, "html.parser")
tag = soup.find(name='div',attrs={"id":"auto-channel-lazyload-article"})
print(tag)





