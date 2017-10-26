#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))

while True:
    back_msg = phone.recv(1024).decode("utf-8")
    print(back_msg)
    if back_msg == "用户名或密码错误！":
        back_msg = phone.recv(1024)
        print(back_msg.decode('utf-8'))
        msg = input('>>>:').strip()
        if not msg:continue
        phone.send(msg.encode('utf-8'))
    else:
        msg = input('>>>:').strip()
        if not msg: continue
        phone.send(msg.encode('utf-8'))
phone.close()


