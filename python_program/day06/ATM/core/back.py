#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from core import logger

lilv = 0.05

def auth(base_dir):
    while True:
        name = input('请输入用户名：')
        pwd = input('请输入密码：')
        lie = os.listdir("%s\db" % base_dir)
        if name not in lie:
            print('用户名或密码错误！')
        else:
            with open('%s\db\%s_back' % (base_dir,name), 'r', encoding='utf-8') as f2:
                data = f2.readline()
            data = eval(data)
            if data['name'] != name or data['pwd'] != pwd:
                print('用户名或密码错误！')
            else:
                balance = data['balance']
                print('您的当前信用卡可用额度为:%s' % balance)
                return (balance,data,name)

def file_update(base_dir,fh,name=None,num=0):
    with open('%s\db\%s' % (base_dir, name), 'r', encoding='utf-8') as read_f, \
            open('%s\db\%s.swap' % (base_dir, name), 'w', encoding='utf-8') as write_f:
        data = read_f.readline()
        data = eval(data)
        if fh == "+":
            data['balance'] = data['balance'] + num
            write_f.write(str(data))
            logger.loger("back", name, num, 0)
        elif fh == "-":
            data['balance'] = num
            write_f.write(str(data))
    os.remove('%s\db\%s' % (base_dir, name))
    os.rename('%s\db\%s.swap' % (base_dir, name), '%s\db\%s' % (base_dir, name))



def enchashment(base_dir,name,yu_e):
        balance,data,name = auth(base_dir)
        num = input("请输入要取现的金额：").strip()
        if len(num) > 0 and num.isdigit():
            num = int(num)
            balance = balance - num - num*lilv
            if balance >= 0:
                data['balance'] = balance
                with open('%s\db\%s_back' % (base_dir, name), 'w', encoding='utf-8') as f:
                    f.write(str(data))
                file_update(base_dir,"+",name,num)
            else:
                print('取款额度超支！')
                return

def repayment():
    pass
#     with open('%s\db\%s_back' % (base_dir, name), 'r', encoding='utf-8') as read_f:
#         data = read_f.readline()
#         data = eval(data)
#         credit
#     print("dang前用户的信用额度为%d,需要还款" %)

def transfer_accounts():
    pass

def bill():
    pass

msg = '''
    1.取现（已实现）
    2.还款
    3.转账
    4.账单
    5.退出
'''
menu_dic = {
    "1":enchashment,
    "2":repayment,
    "3":transfer_accounts,
    "4":bill,
    "5":5
}
def atm(base_dir,name,yu_e):
    while True:
        print(msg)
        choice = input('选项>>>').strip()
        if len(choice) == 0 or choice not in menu_dic: continue
        if choice == "5":break
        menu_dic[choice](base_dir,name,yu_e)


