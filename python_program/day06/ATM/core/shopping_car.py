#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import getpass
import re
from core import menu
from core import back
from core import logger

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

li = []
f1 = open('%s\db\goods'% base_dir, 'r',encoding='utf-8')
data = f1.readlines()
for i in data:
    li.append(i)
f1.close()

goods_name = []
for goods_1 in li:
    goods_name.append(goods_1.split(' ')[1])

def run(base_dir):
    stop = True
    while stop:
        name = input('请输入用户名：')
        pwd = input('请输入密码：')
        lie = os.listdir("%s\db" % base_dir)
        if name not in lie:
            print('用户名或密码错误！')
        else:
            with open('%s\db\%s'% (base_dir,name),'r',encoding='utf-8') as f2:
                data = f2.readline()
            data = eval(data)
            if data['name'] != name or data['pwd'] != pwd:
                print('用户名或密码错误！')
            else:
                balance = data['balance']
                print('您的当前的账户余额为:%s' % balance)
                menu.menu(base_dir,name,balance)
                stop = False

def buy(base_dir,name=None,yu_e=0):
    with open('%s\db\%s' % (base_dir, name), 'r', encoding='utf-8') as f2:
        data = f2.readline()
    data = eval(data)
    balance = data['balance']
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
                f = open('%s\db\goods'% base_dir, 'r',encoding='utf-8')
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
                    print(i, end='')
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
                            menu.menu(base_dir, name, balance)
                        else:
                            choice = input("""
    商品已加入购物车。
    结账请输入2，继续购物按任意键：""")
                            if choice == '2':
                                print('您购买的商品有%s,您的余额为：%s,欢迎下次光临！' % (goods, balance))
                                back.file_update(base_dir, "-", name, balance)
                                logger.loger("shop", name, balance, goods)
                                stop = False
                                break
                            else:
                                pass
