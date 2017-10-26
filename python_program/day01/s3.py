#!/usr/bin/env python
#-*- coding:utf-8 -*-

# i=1
# while i< 11:
#     print(i)
#     i += 1
#     if i == 7:
#         i += 1
#         continue

# value=0
# i=1
# while i < 101:
#     if i % 2 == 1:
#         pass
#     else:
#         value = value + i
#     i += 1
#
# print(value)

countent = "i am a yongshi"
if "yongshi" in countent:
    print("True")
else:
    print(False)

value = " hahah ha  "
new_value = value.strip()
print('new_value')

user_info = 'sadj,sadj,sajd,sad'
v = user_info.rsplit(',',1)
print(v)

l = len(user_info)
print(l)

i=0
while i < l:
    print(user_info[i])
    i += 1





