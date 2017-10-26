#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
from urllib import request

IP=["46.105.110.226(法国)","52.62.100.154(澳大利亚)","88.208.229.75(英国)","185.102.219.3(德国)","23.111.154.90(弗罗里达)","192.1    24.18.58(西雅图)","221.228.109.54(无锡云主机)","101.251.247.46(北京云主机)","148.153.1.74(洛杉矶云主机)","173.45.34.7(la)","69.16    9.34.21(dc)"]

for i in IP:
        response = request.urlopen(r'http://%s/approve/monitor' % i.split("(")[0])
        page = response.read()
        page = eval(page.decode('utf-8'))
        data = page["data"]
        print("----------%s----------" % i)
        #with open(os.path.dirname(os.path.realpath(__file__)) + "/monitor.json", "w",encoding='utf-8') as F:
        for k in data:
            for K in data[k]:
                if int(data[k][K]) != 0:
                    dic = {}
                    dic[k] = {K:data[k][K]}
                    print(dic)
       # os.remove(os.path.dirname(os.path.realpath(__file__)) + "/monitor.json")
