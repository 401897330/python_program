#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import socket
import struct
import json
import sys
import time

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ftp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ftp_client.connect(('127.0.0.1', 8080))

cmd_li = ["ls", "cd", "rm", "put", "get", "quit", "exit"]

def progress_bar(num):
    sys.stdout.write('%s\r' % ('#' * num))

    sys.stdout.flush()

def get(cmd, conn):
    conn.send(cmd.encode('utf-8'))
    head_struct = conn.recv(4)
    head_len = struct.unpack('i', head_struct)[0]
    head_bytes = conn.recv(head_len)
    head_json = head_bytes.decode('utf-8')
    head_dic = json.loads(head_json)
    if head_dic["filename"] == None:
        total_size = head_dic['total_size']
        recv_size = 0
        data = b''
        while recv_size < total_size:
            recv_data = ftp_client.recv(1024)
            data += recv_data
            recv_size += len(recv_data)
        print(data.decode('utf-8'))
    else:
        total_size = head_dic['filesize']
        file_name = head_dic['filename']
        user_name = head_dic['user_name']

        file_path = r"%s\db\%s\%s" % (base_dir, user_name, file_name)
        recv_size = 0
        with open(file_path, 'wb') as f:
            while recv_size < total_size:
                recv_data = conn.recv(1024)
                f.write(recv_data)
                recv_size += len(recv_data)
                num = float(recv_size) / float(total_size)
                num_2 = int(num * 50)
                progress_bar(num_2)
            sys.stdout.write('\n')
            sys.stdout.flush()
            print("upload successful!")


def put(cmd, conn):
    conn.send(cmd.encode('utf-8'))
    head_struct = conn.recv(4)
    head_len = struct.unpack('i', head_struct)[0]
    head_bytes = conn.recv(head_len)
    head_json = head_bytes.decode('utf-8')
    head_dic = json.loads(head_json)

    if head_dic["filename"] == None:
        total_size = head_dic['total_size']
        recv_size = 0
        data = b''
        while recv_size < total_size:
            recv_data = ftp_client.recv(1024)
            data += recv_data
            recv_size += len(recv_data)
        print(data.decode('utf-8'))
    else:
        total_size = head_dic['filesize']
        file_name = head_dic['filename']
        user_name = head_dic['user_name']

        file_path = r"%s\db\ftp\%s" % (base_dir, file_name)
        recv_size = 0
        with open(file_path, 'wb') as f:
            while recv_size < total_size:
                recv_data = conn.recv(1024)
                f.write(recv_data)
                recv_size += len(recv_data)
                num = float(recv_size) / float(total_size)
                num_2 = int(num * 50)
                progress_bar(num_2)
            sys.stdout.write('\n')
            sys.stdout.flush()
            print("upload successful!")

stop = True
while stop:
    back_msg = ftp_client.recv(1024).decode("utf-8")
    print(back_msg)
    if back_msg == "用户名或密码错误！":
        back_msg = ftp_client.recv(1024)
        print(back_msg.decode('utf-8'))
        cmd = input('>>>:').strip()
        if not cmd: continue
        ftp_client.send(cmd.encode('utf-8'))
    elif "登陆成功" in back_msg:
        user_name = back_msg.split(" ")[0]
        while True:
            cmd = input('输入\033[1;31m help \033[0m查看支持的命令>>>:').strip()
            if not cmd: continue
            cmd_1 = cmd.split(" ")[0].lower()
            if cmd_1 == "put":
                put(cmd, ftp_client)
            elif cmd_1 == "get":
                get(cmd, ftp_client)
            else:
                if cmd_1 == "ls":
                    cmd = "dir"
                if cmd_1 == "rm" and cmd.split(' ')[-1] == "":
                    print("不能以空结尾！")
                    continue
                if cmd_1 == "help":
                    print(cmd_li)
                    continue
                if cmd_1 == "exit" or cmd_1 == "quit":
                    stop = False
                    break
                ftp_client.send(cmd.encode('utf-8'))
                head_struct = ftp_client.recv(4)

                head_len = struct.unpack('i', head_struct)[0]
                head_bytes = ftp_client.recv(head_len)
                head_json = head_bytes.decode('utf-8')
                head_dic = json.loads(head_json)

                total_size = head_dic['total_size']
                recv_size = 0
                data = b''
                while recv_size < total_size:
                    recv_data = ftp_client.recv(1024)
                    data += recv_data
                    recv_size += len(recv_data)
                print(data.decode('gbk'))
    else:
        cmd = input('>>>:').strip()
        if not cmd: continue
        ftp_client.send(cmd.encode('utf-8'))
ftp_client.close()