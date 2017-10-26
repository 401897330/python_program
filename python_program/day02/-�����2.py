#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1.
# li = ['alex','eric','rain']
# s = '_'.join(li)
# print(s)
# alex_eric_rain


#2.
# li = ['alex','aric','Alex','Tony','rain',' kyo',' mary ','  Aric ']
# ko = []
# for i in li:
#     a = i.strip().lower().startswith("a")
#     b = i.strip().lower().endswith('c')
#     if a == True and b == True:
#         ko.append(i)
# print(ko)


#4
# li = ['hello','seven',['mon',['h','Kelly'],'all'],123,456]
# print(li[2][1][1])
# li[2][2] = 'ALL'
# print(li)


#7
# dic = {'k1': 'v1', 'k2': 'v2', 'k3': [11, 22, 33]}
# for i in dic:
#     print(i)
# print(list(dic.values()))
# dic['k4'] = 'v4'
# print(dic)
# dic['k1'] = 'alex'
# print(dic)
# dic['k3'].append(44)
# print(dic)
# dic['k3'].insert(0,18)
# print(dic)



#8
# a = 'alex'
# li = list(a)
# tu = tuple(a)
# li_2 = ['alex','serven']
# tu_2 = tuple(li)
# tu_3 = ('Alex','serven')
# li_3 =  list(tu_3)
# print(li,tu,tu_2,li_3)


#9.
# li = [11,22,33,44,55,66,77,88,99]
# di = {}
# l2 = []
# l3 = []
# for i in li:
#     if i >66:
#        l2.append(i)
#     else:
#         l3.append(i)
# di['k1'] = l2
# di['k2'] = l3
# print(di)


#12
# 空字符串''和空列表[]空元祖()空字典{} 是布尔类型的False
# 整数类型0为False 其余为True



#13
# l1 = [11,22,33]
# l2 = [22,33,44]
# v = []
# for i in l1:
#     if i not in l2:
#         v.append(i)
# print(v)
#
# v2 = []
# for i in l1:
#     if i in l2:
#         v2.append(i)
# print(v2)




#14.
# li = []
# for i in range(1,101):
#     li.append(i)
# print(li)
# li.sort(reverse=True)
# print(li)

# li = []
# i = 1
# while i <= 100:
#     li.append(i)
#     i += 1
# print(li)
# li.sort(reverse=True)
# print(li)



#16
# li = []
# for i in range(1,100):
#     li.append("alex%s alex%s@live.com pwd%s" % (i,i,i))
# p = int(input('请输入页码：'))
# start = (p -1) * 10
# end = p * 10
# v1 = li[start:end]
# for i in v1:
#     print(i)


#17.
# li = [2,4,5,6,8,7,9]
# c = []
# for i in li:
#     for j in li:
#         a = str(i) + str(j)
#         b = str(j) + str(i)
#         if a != b:
#             c.append(a)
# print(len(c))


#18
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s * %s = %s"% (i,j,i*j),end=" ")
#     print(" ")


#19.
# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# li = []
# li_2 = []
# for i in num:
#     li.append(i)
#     for j in num:
#         if j in li:
#             pass
#         else:
#             add = i + j
#             if add == 9:
#                 li_2.append((i,j))
# print(li_2)


#20
# gj = 5
# mj = 3
# i = 1
# di = {}
# while i < 100/gj:
#     total = 100 - gj*i
#     j = 1
#     while j < total/mj:
#         xj = (total - mj*j)*3
#         di['公鸡'] = i
#         di['母鸡'] = j
#         di['小鸡'] = xj
#         j += 1
#         print(di)
#     i += 1







