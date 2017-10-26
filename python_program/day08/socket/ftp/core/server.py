#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import time
import socket
import subprocess
import struct
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ftp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ftp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ftp.bind(('127.0.0.1', 8080))
ftp.listen(5)



def baotou(cmd_res, conn):
    head_dic = {'filename': None, 'user_name': None, 'total_size': len(cmd_res)}
    head_json = json.dumps(head_dic)
    head_bytes = head_json.encode('utf-8')
    conn.send(struct.pack('i', len(head_bytes)))
    conn.send(head_bytes)
    conn.send(cmd_res)


def cd(parameter , user_name, conn):

    dir_name = os.listdir('%s\db' % base_dir)
    if parameter == None:
        parameter = user_name
    if parameter not in dir_name:
        msg = "没有权限！只允许在家目录和ftp目录切换！"
        return msg
    path = "%s\db\%s" %(base_dir, parameter)
    os.chdir(path)
    msg = "change dir！"
    return msg

def rm(parameter , user_name, conn):
    dir_name = os.listdir('%s\db\%s' % (base_dir, user_name))
    if parameter not in dir_name:
        msg = "文件不存在！用户只能删除自己家目录下的文件！"
        return msg
    file_name = "%s\db\%s\%s" % (base_dir, user_name, parameter)
    os.remove(file_name)
    msg = "已删除文件%s" % parameter
    return msg

def get(parameter, conn, user_name):
    path = r"%s\db\ftp" % base_dir
    file_name = os.listdir(path)
    if parameter not in file_name:
        msg = "文件不存在!".encode('utf-8')
        baotou(msg, conn)
    else:
        file_size = os.path.getsize('%s\%s' % (path, parameter))
        head_dic = {'user_name': user_name, 'filename': parameter, 'filesize': file_size}
        head_json = json.dumps(head_dic)
        head_bytes = head_json.encode('utf-8')
        conn.send(struct.pack('i', len(head_bytes)))
        conn.send(head_bytes)
        with open('%s\%s' % (path, parameter), "rb") as f:
            for line in f:
                conn.send(line)

def put(parameter, conn, user_name):
    path = r"%s\db\%s" % (base_dir, user_name)
    file_name = os.listdir(path)
    if parameter not in file_name:
        msg = "文件不存在!".encode('utf-8')
        baotou(msg, conn)
    else:
        file_size = os.path.getsize('%s\%s' % (path, parameter))
        head_dic = {'user_name': user_name, 'filename': parameter, 'filesize': file_size}
        head_json = json.dumps(head_dic)
        head_bytes = head_json.encode('utf-8')
        conn.send(struct.pack('i', len(head_bytes)))
        conn.send(head_bytes)
        with open('%s\%s' % (path, parameter), "rb") as f:
            for line in f:
                conn.send(line)

cmd_dic = {"cd": cd,
           "get": get,
           "put": put,
           "get": get,
           "rm": rm
           }

while True:
    conn, addr = ftp.accept()
    stop = True
    while stop:
        try:
            conn.send("请输入用户名：".encode('utf-8'))
            user_name = conn.recv(1024).decode('utf-8')
            conn.send("请输入密码：".encode('utf-8'))
            pwd = conn.recv(1024).decode('utf-8')
            li = []
            li.append(user_name)
            li.append(pwd)
            user_db = ':'.join(li)
            with open(r'%s\db\user_db' % base_dir, 'r', encoding='utf-8') as f:
                data = f.read()
            if user_db in data:
                msg = "%s 登陆成功！" % user_name
                conn.send(msg.encode('utf-8'))
                print("用户%s已登录系统。" % user_name)
                while True:
                    cmd = conn.recv(1024).decode('utf-8')
                    if not cmd: break
                    if len(cmd.split(" ")) > 1:
                        parameter = cmd.split(" ")[-1]
                        cmd = cmd.split(" ")[0]
                    else:
                        parameter = None
                    if cmd == "cd":
                        cmd_res = cmd_dic[cmd](parameter, user_name, conn).encode("gbk")
                        baotou(cmd_res, conn)
                    elif cmd == "rm":
                        cmd_res = cmd_dic[cmd](parameter, user_name, conn).encode("gbk")
                        baotou(cmd_res, conn)
                    elif cmd == "put":
                        put(parameter, conn, user_name)
                    elif cmd == "get":
                        get(parameter, conn, user_name)
                    else:
                        res = subprocess.Popen(cmd, shell=True,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                        err = res.stderr.read()
                        if err:
                            cmd_res = err
                        else:
                            cmd_res = res.stdout.read()
                        baotou(cmd_res, conn)
            else:
                conn.send("用户名或密码错误！".encode('utf-8'))
        except Exception:
            break
    conn.close()
    print('用户%s已断开连接。'% user_name)
ftp.close()