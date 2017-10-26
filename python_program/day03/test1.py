#!/usr/bin/env python
#-*- coding:utf-8 -*-
# f = open('a.txt',encoding='utf-8')
# data = f.read()
# print(data)
# f.seek(0)
# data2 = f.readlines()
# print(data2)

# num = 16
# user_msg = "alex,40,1522935433,老师,2005-09-27"
# with open("user_db","a",encoding="utf-8") as f:
#     f.write('%s,%s' % (num, user_msg))

sql = 'select * from user_db where id >= 10 and id <= 20'
if '>=' in sql:
    print('ok')
# tiaojian = sql.split('<')[1].strip()
# print(tiaojian)

a = [0,1,2,3,4,5,6]
print(a[5:])

# def open_file(file_name):
#     with open("%s" % (file_name), "r",encoding='utf-8') as f:
#         data = f.readlines()
#     return data
#
# file_name = sql.split('from')[1].strip().split(' ')[0].strip()
# data_2 = open_file(file_name)
# title = data_2[0]
# print(title)
# print(title.index('name'))













