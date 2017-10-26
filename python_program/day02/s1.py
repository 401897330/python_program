#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# a = 'Yongshi{0}{2}{1}'
# print(a.endswith('shi'))
# print(a.capitalize())
# print(a.casefold())
# print(a.center(30,'&') )
# print('_'.join(a) )
# print(a.isdigit())
# print(a.upper())
# print(a.lower())
# print(a.count('n'))
# print(a.format('勇士','kyo','terry'))
# print(a.ljust(20,'*'))
# name = ' aleX '
# print(name.strip())
# print(name.startswith('al'))
# print(name.endswith('X '))
# print(name.replace('l','p'))
# print(name.partition('l'))
# print(name.upper())
# print(name.lower())
# user_list = ['李泉','刘一','刘康','豆豆','小龙']
# user_list.append('刘铭')
# print(user_list)
# v = user_list.clear()
# print(user_list)
# v = user_list.copy()
# print(v)
# print(user_list)
# print(user_list.count('刘一'))
# user_list.extend(['勇士','alex'])
# print(user_list)
# print(user_list.index('alex'))
# user_list.remove('alex')
# print(user_list)
# v = user_list.pop(2)
# print(v)
# print(user_list)
# user_list.reverse()
# print(user_list)

# for i in range(1,11):
#     print(i)
#
# for i in range(1,11,2):
#     print(i)
# for i in range(10,0,-1):
#     print(i)
#
# user_tuple = ['alex','eric',(1,2,3),'seven','alex']
# for i in user_tuple:
#     print(i)
# v = user_tuple[0]
# v = user_tuple[0:3]
# print(v)
# del user_tuple[2]
# print(user_tuple)
# import re
# f = open('E:\python项目\day02\goods', 'r')
# text=f.read()
# f.close()
# tofind=input("please input yo want to find:")
# tofind=re.escape(tofind)
# result=re.findall(".*"+tofind+".*",text)
# print(result)
# for line in result:
#     print(line)

tofind = input('>>>')
p = tofind.isdigit()
print(p)









