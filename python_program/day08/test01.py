#!/usr/bin/env python
#-*- coding:utf-8 -*-

# class List(list):
#     def __init__(self, item, tag=False):
#         super().__init__(item)
#         self.tag = tag
#
#     def append(self, p_object):
#         if not isinstance(p_object, str):
#             raise TypeError('%s must be str' % p_object)
#         super().append(p_object)
#
#
# class_name = 'Chinese'
# class_bases = (object,)
# class_body = '''
# country = 'China'
# def __init__(self,name,age):
#     self.name = name
#     self.age = age
# def talk(self):
#     print("%s is talking" % self.name)
# '''
# class_dic={}

import sys,time
import os

# for i in range(50):
#     sys.stdout.write('%s\r' %('#'*i))
#     sys.stdout.flush()
#     time.sleep(0.1)
path = "E:\python项目\day08\套接字\作业ftp服务器"
parameter = "core\client.py"
a = os.path.getsize('%s\%s' % (path, parameter))
c = os.path.basename(parameter)
print(a, c)
os.remove(r'E:\python项目\day08\套接字\作业ftp服务器\db\ftp\django.pdf')



if __name__ == '__main__':
    control.py.mysql_login()









