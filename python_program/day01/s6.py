#!/usr/bin/env python
#-*- coding:utf-8 -*-
name = " alex"
age = name.strip().capitalize()
print(name)
print(age)
print(name.replace('l','p'))
print(name.split('l'))
print(name.partition('l'))
print(name.startswith(" al"))
print(name.lower())
print(name.upper())
print(name[1])
print(name[0:3])
print(name[-2:])
print(name.index('e'))
print(name[:-1])
for i in name:
    print(i)
li = ['alex','eric','rain']
print('_'.join(li))


while True:
    def check_code():
        import random
        checkcode = ''
        for i in range(4):
            current = random.randrange(0, 4)
            if current != i:
                temp = chr(random.randint(65, 90))
            else:
                temp = str(random.randint(0, 9))
            checkcode += temp
        return checkcode
    code = check_code()
    print(code)
    s = input('>>>')
    if s == code:
        print('welcome!')
        break
    else:
        print('验证码输入错误，请重新输入！')


word = ['东京热','苍老师']
s = input('>>>')
for i in word:
    if i in s:
        s = s.replace(i,'***')
    else:
        s = s
print(s)

