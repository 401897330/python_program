#!/usr/bin/env python
#-*- coding:utf-8 -*-
#1.
#chmod +x 脚本  ./脚本         python 脚本


#2
#i字节=8位


#3
#ASCII码使用一个字节编码，所以它的范围基本是只有英文字母、数字和一些特殊符号 ，只有256个字符。
#Unicode能够表示全世界所有的字节
#UTF-8（8-bit Unicode Transformation Format）是一种针对Unicode的可变长度字符编码，又称万国码
#GBK是只用来编码汉字的，GBK全称《汉字内码扩展规范》，使用双字节编码。


# 4.
# utf-8占位3字节    gbk占2位

# 5.
# 单行注释用#号，多行注释用''' ''' 或者""" """



# 6.
# 变量只能是字母、数字和下划线组成的，数字不能开头。
# 变量名不能是python内置关键字


# 8.
# True 和 False


# 9.
# a = "alex"
# b = a.capitalize()
# print(a)
# print(b)
# 结果输出 ：alex  Alex


# 10.
# name = ' alex'
# a.  name.strip()
# b.  name.startswith("al")
# c.  name.endtswith("X")
# d.  name.capitalize('l',"p")
# e.  name.split('l') name.partition('l')
# f.  列表
# g.  name.upper()
# h.  name.lower()
# i.  name[1]
# j.  name[2]
# k.  name[-2:]
# l.  name.index('e')
# m.  name[0:-1]


# 11.
# a = 'alex'
# for i in a:
#     print(i)
# 输出 a l e x


# 12.
# li = ['alex','eric','rain']
# s = '_'.join(li)
# print(s)
# alex_eric_rain


# 13.
# python2中的range返回一个list  python3返回一个迭代对象



# 18.
# while True:
#     def check_code():
#         import random
#         checkcode = ''
#         for i in range(4):
#             current = random.randrange(0, 4)
#             if current != i:
#                 temp = chr(random.randint(65, 90))
#             else:
#                 temp = str(random.randint(0, 9))
#             checkcode += temp
#         return checkcode
#     code = check_code()
#     print(code)
#     s = input('>>>')
#     if s == code:
#         print('welcome!')
#         break
#     else:
#         print('验证码输入错误，请重新输入！')


# 19.
# word = ['东京热','苍老师']
# s = input('>>>')
# for i in word:
#     if i in s:
#         s = s.replace(i,'***')
#     else:
#         s = s
# print(s)