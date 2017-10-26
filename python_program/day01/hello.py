#！/usr/bin/env python
#-*- coding:utf-8 -*-


li = ['alex', 'terry',' kyo','eric']
li.append('seven')
li.insert(0,'Tony')
li.insert(1,'Kelly')
del li[2:4]
for i in range(len(li)):
    print(i,li[i])
for k,v in enumerate(li,100):
    print(k,v)
print(li[1].upper())
print(li)

tu = ('alex','eric','rain')
print(len(tu))
print(tu[1])
for i,o in enumerate(tu,10):
    print(i,o)

dic = {'k1':'alex','k2':'eric','k3':'terry'}
for i in dic.values():
    print(i)

a = 'alex'
print(list(a))
