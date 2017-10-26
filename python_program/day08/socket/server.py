#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import socket
base_dir = os.path.dirname(os.path.abspath(__file__))

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8080))
phone.listen(5)

while True:
    conn, addr = phone.accept()
    while True:
        conn.send("请输入用户名：".encode('utf-8'))
        user_name = conn.recv(1024).decode('utf-8')
        conn.send("请输入密码：".encode('utf-8'))
        pwd = conn.recv(1024).decode('utf-8')
        li = []
        li.append(user_name)
        li.append(pwd)
        user_db = ':'.join(li)
        with open(r'%s\作业ftp服务器\db\user_db' % base_dir,'r',encoding='utf-8') as f:
            data = f.read()
        print(data)
        print(user_db)
        if user_db in data:
            conn.send("欢迎登陆！".encode('utf-8'))
            while True:
                try:
                    client_msg = conn.recv(1024)
                    if not client_msg:break
                    conn.send(client_msg.upper())
                except Exception:
                    break
            conn.close()
        else:
            conn.send("用户名或密码错误！".encode('utf-8'))
phone.close()



