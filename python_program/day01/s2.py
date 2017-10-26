#!/usr/bin/env python
#-*- coding:utf-8 -*-
import getpass

user_name = input('请输入用户名：')
pwd = getpass.getpass('请输入密码：')
if user_name == 'yongshi' and pwd == '090425':
    print('welcome')
else:
    print('滚')

