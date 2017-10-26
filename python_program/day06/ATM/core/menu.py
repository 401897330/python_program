#!/usr/bin/env python
#-*- coding:utf-8 -*-

from core import shopping_car
from core import back

def menu(base_dir,name,balance):
    while True:
        print('''
        1.购物
        2.银行账户管理
        3.退出
        ''')
        menu_dic = {
            "1":shopping_car.buy,
            "2":back.atm,
            "3":exit
        }
        choice = input('请输入您要选择的操作：').strip()
        if len(choice) == 0 or choice not in menu_dic:continue
        if choice == "3":break
        menu_dic[choice](base_dir,name,balance)
