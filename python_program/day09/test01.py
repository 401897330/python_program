#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# import paramiko
#
# ssh = paramiko.SSHClient()
#
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh.connect("192.168.1.40",22,"root", "090425")
#
# stdin, stdout, stderr = ssh.exec_command("df -Th")
# if stderr:
#     for err_msg in stderr.readlines():
#         print(err_msg,end='')
# for msg in stdout.readlines():
#     print(msg,end='')
#
# ssh.close()
#
while True:
    a=input('>>>').strip()
    print(a)
    if not a:break














