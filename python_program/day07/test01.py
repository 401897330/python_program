#!/usr/bin/env python
#-*- coding:utf-8 -*-

# class student():
#     count = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def count(self):
#         pass
#
# class Hero():
#     country = "德玛西亚"
#     def __init__(self,name):
#         self.name = name
#
#     def run(self):
#         print("%s is run"% self.name)
# dema = Hero
# print(dema.run(dema))



# class Foo():
#     @classmethod
#     def test(cls):
#         print(cls)
# f=Foo()
# f.test()
#
# class Foo:
#     @staticmethod
#     def test(x,y):
#         print("test",x,y)
# f=Foo()
# f.test(1,10)

# import setting
# class MySQL:
#     def __init__(self,host,port):
#         self.host = host
#         self.port = port
#         print('conneting...')
#     @classmethod
#     def from_conf(cls):
#         return cls(setting.HOST,setting.PORT)
#     def select(self):
#         print(self)
#         print('select function')
# conn1 = MySQL('192.168.1.100',3306)
# conn2 = MySQL.from_conf()


# class foo:
#     def test(self):
#         print(self.__name__)
#
# class A(foo):
#     pass
#
# a=A
# a.test(A)




