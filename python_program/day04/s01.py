#!/usr/bin/env python
#-*- coding:utf-8 -*-
# def  select():
#     print('select')
#
# def insert():
#     print('insert')
#
# def delete():
#     print('delete')
#
# def update():
#     print('update')
#
# dic = {
#     'select':select,
#     'insert':insert,
#     'delete':delete,
#     'update':update
# }
#
# while True:
#     sql = print('sql>>')
#     l = sql.split()
#     if l[0] in dic:
#         dic[l[0]]()
#
# x=1
# y=2
# def f1():
#     x=1
#     y=2
#     def f2():
#         print(x,y)
#     return f2
# f=f1()
# print(f.__closure__[0].cell_contents)
#
#
from urllib.request import urlopen

def index(url):
    def get():
        return urlopen(url).read()
    return get()
oldboy = index('http://www.baidu.com')
print(type(oldboy))
print(oldboy)
print('OK')
# print(oldboy().decode('utf-8'))
# print(oldboy.__colsure__[0].cell_contents)


# import time
#
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         res = func(*args,**kwargs)
#         stop_time = time.time()
#         print('run time is %s'% (stop_time-start_time))
#     return wrapper
#
# # @timmer  # index=timmer(index)
# # def index():
# #     time.sleep(3)
# #     print('welcome to index')
# #     return 1
#
# @timmer
# def foo(name):
#     time.sleep(1)
#     print('from foo')
#
#
#
# while True:
#     name = input('name>>').strip()
#     pwd = input('pwd>>').strip()
#     if name == 'egon' and pwd == '123456':
#         resl=foo('egon')
#         print(resl)
#         break
#     else:
#         print('Error')

