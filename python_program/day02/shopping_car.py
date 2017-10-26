#!/usr/bin/env python
#-*- coding:utf-8 -*-

import getpass
import re

li = []
f1 = open('E:\python项目\day02\goods', 'r',encoding='utf-8')
data = f1.readlines()
for i in data:
    li.append(i)
f1.close()

goods_name = []
for goods_1 in li:
    goods_name.append(goods_1.split(' ')[1])
def run():
    stop = True
    while stop:
        name = input('请输入用户名：')
        pwd = input('请输入密码：')
        f2 = open('E:/python项目/day02/user_db', 'r')
        data = f2.read()
        f2.close()
        user_info = {}
        user_str = data.split('\n')

        for i in user_str:
            temp = i.split('|')
            if temp == ['']:
                pass
            else:
                user_info[temp[0]] = {'pwd': temp[1], 'balance': temp[2]}
        if user_info[name]['pwd'] != pwd:
            print('用户名或密码错误！')
        else:
            yu_e = user_info[name]['balance']
            print('您的当前的余额为:%s' % yu_e)
            balance = int(yu_e)
            goods = []
            while True:
                tofind = input('请输入商品页码,或者商品名称：').strip()
                if len(tofind) == 0:
                    continue
                elif tofind == 'q':
                    stop = False
                    break
                else:
                    p = tofind.isdigit()
                    if p == False:
                        f = open('E:\python项目\day02\goods', 'r',encoding='utf-8')
                        text = f.read()
                        f.close()
                        tofind = re.escape(tofind)
                        result = re.findall(".*" + tofind + ".*", text)
                        if result == []:
                            print("没有此商品信息。")
                            continue
                        else:
                            for line in result:
                                print(line)
                    else:
                        start = (int(tofind) - 1) * 10
                        end = int(tofind) * 10
                        v1 = li[start:end]
                        for i in v1:
                            print(i)
                    num = input('请输入要购买的商品编号:')
                    pd = num.isdigit()
                    if num == 'q':
                        stop = False
                        break
                    else:
                        if pd == False:
                            print('输入错误！')
                            continue
                        else:
                            if int(num) > len(li):
                                print('没有此商品，请重新输入！')
                            else:
                                num2 = int(num) - 1
                                sp = li[num2].split(' ')[1]
                                goods.append(sp)
                                price = li[num2].split(' ')[2]
                                balance = balance - int(price)
                                if balance < 0:
                                    print('余额不足，请充值！')
                                    break
                                else:
                                    choice = input("""
        商品已加入购物车。
        结账请输入2，继续购物按任意键：""")
                                    if choice == '2':
                                        print('您购买的商品有%s,您的余额为：%s,欢迎下次光临！' % (goods,balance))
                                        f3 = open('E:/python项目/day02/user_db', 'w')
                                        user_info[name]['balance'] = balance
                                        for j in user_info:
                                            f3.write("%s|%s|%s%s" % (j,user_info[j]['pwd'],user_info[j]['balance'],'\n'))
                                        f3.close()
                                        stop = False
                                        break
                                    else:
                                        pass
