#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
import struct
import json

ftp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ftp.connect(('127.0.0.1',8080))

while True:
    cmd=input('>>: ').strip()
    if not cmd:continue
    ftp.send(cmd.encode('utf-8'))


    head_struct=ftp.recv(4)
    head_len=struct.unpack('i',head_struct)[0]


    head_bytes=ftp.recv(head_len)
    head_json=head_bytes.decode('utf-8')
    head_dic=json.loads(head_json)


    print(head_dic)
    total_size=head_dic['total_size']
    recv_size=0
    data=b''
    while recv_size < total_size:
        recv_data=ftp.recv(1024)
        data+=recv_data
        recv_size += len(recv_data)
    print(data.decode('gbk'))
phone.close()