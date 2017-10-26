#!/usr/bin/env python
#-*- coding:utf-8 -*-
#练习题1
v1 = [11,22,33,44,55,66,77,88,99,90]
v2 = {'key1':[],'key2':[]}
for item in v1:
    if item > 66:
        v2['key1'].append(item)
    else:
        v2['key2'].append(item)
print(v2)


#练习题2

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
f1 = open('E:\python项目\day01\db','w')
i = 1
for item in goods:
    name = item['name']
    price = item['price']
    f1.write("%i %s %s %s" % (i,name,price,'\n'))
    i += 1
f1.close()

def get_num(num):
    if int(num) > 5:
        print('没有此商品，请重新输入！')
    else:
        num2 = int(num) - 1
        price = goods[num2]["price"]
        yue = int(total) - price
        return yue

total = input('请输入总资产：')
while True:
    f2 = open('E:\python项目\day01\db', 'r')
    data = f2.read()
    print(data)
    f2.close()
    num = input('请输入要购买的商品编号:')
    total = get_num(num)
    if total < 0:
        print('余额不足，请充值！')
        break
    else:
        choice = input("""
商品已加入购物车。
结账请输入2，继续购物输入1：""")
        if choice == '2':
            print('您的余额为：%s,欢迎下次光临！' % total)
            break
        else:
            pass

#练习题3

dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    }
    "河南": {
        "["原阳","延津封丘]"
    }
    "山西": {
        ""
    }
}
for v in dic.keys():
    print(v)
inp = input('>>>')
dic[inp]









