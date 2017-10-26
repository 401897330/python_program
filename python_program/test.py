#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import os
import sys
# data = {"data":[]}
# for i in range(1, 24):
#     data["data"].append({"request_time":"2017-10-17 %s:%s:30" % (i, i), "ip":"100.100.100.100", "sn_addr":"US" ,"channel":"CCTV1" ,"stream":"8000", "request_addr":"la", "sn":"142030000110", "ht":"True", "status":"200", "down_time":"5.123", "ts_num":"12345.ts", "netspeed":"2M"})
#
# print(data)
# response = requests.post("http://127.0.0.1:8080/suntv/BoxInfo/", json=data)
# print(response.text)


import asyncio
import requests

IP=["88.208.229.75(英国)","185.102.219.3(德国)","103.4.16.107(澳大利亚)","23.111.154.90(弗罗里达)","192.124.18.58(西雅图)","221.228.109.54(无锡云主机)","101.251.247.46(北京云主机)","148.153.1.74(洛杉矶云主机)","173.45.34.7(la)","69.169.34.21(dc)"]

@asyncio.coroutine
def fetch_async(func, *args):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, func, *args)
    response = yield from future
    print(response.url, response.text)

tasks = []
for ip in IP:
    tasks.append(fetch_async(requests.get, 'http://%s/approve/monitor' % ip.split("(")[0]))

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
