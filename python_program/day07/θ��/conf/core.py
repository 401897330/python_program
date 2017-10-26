#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pickle
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class School:
    def __init__(self, school_name, addr, kecheng, ther):
        self.school_name = school_name
        self.addr = addr
        self.kecheng = kecheng
        self.ther = ther

    def __str__(self):
        return (self.school_name, self.addr, self.kecheng, self.ther)

    def save(self):
        pickle.dump(self, open(r'%s\db\school\%s_%s' % (base_dir, self.school_name, self.addr), 'wb'))

    @staticmethod
    def get_all_obj_list():
        ret = []
        for file_name in os.listdir(r'%s\db\school'% base_dir):
            obj = pickle.load(open(r'%s\db\school\%s' % (base_dir, file_name), 'rb'))
            ret.append(obj)
        for i in ret:
            for j in i.kecheng:
                print("学校名：%s 学校地址：%s  学校包含课程：%s 课程学费：%s 课程学习周期：%s " % (i.school_name, i.addr, j.name, j.price, j.outline))


class Teacher:
    def __init__(self, name, banji, xuexiao):
        self.name = name
        self.banji = banji
        self.xuexiao = xuexiao


class Course:
    def __init__(self, name, price, outline):
        self.name = name
        self.price = price
        self.outline = outline


class Student(School):
    def __init__(self, name, kecheng):
        self.name = name
        self.kecheng = kecheng

    def save(self):
        li = os.listdir(r'%s\db\student' % base_dir)
        num = len(li) + 1
        pickle.dump(self, open(r'%s\db\student\%s_%s' % (base_dir, self.name, num), 'wb'))
        print("学员%s你好，你是第%s个注册的学员，你的的学号为:%s" % (self.name, num, num))

def get_obj_list(name):
    ret = []
    for file_name in os.listdir(r'%s\db\school' % base_dir):
        obj = pickle.load(open(r'%s\db\school\%s' % (base_dir, file_name), 'rb'))
        ret.append(obj)
    for i in ret:
        for j in i.kecheng:
            obj = pickle.load(open(r'%s\db\student\%s' % (base_dir, name), 'rb'))
            if j.name == obj.kecheng:
                print("学员：%s 所在学校名：%s 学校地址：%s  课程：%s 课程学费：%s 课程学习周期：%s " % (obj.name, i.school_name, i.addr, j.name, j.price, j.outline))
                break


def student():
    while True:
        print('''
           1.登陆
           2.注册账户
           3.返回
           ''')
        choice = input('请输入您要选择的操作:').strip()
        if choice == "1":
            while True:
                name = input("输入学员的姓名,按“q”返回上一级：：").strip()
                if name.lower() == "q":
                    break
                num = input("输入学号：").strip()
                file_name = "_".join((name, num))
                if file_name not in os.listdir(r'%s\db\student'% base_dir):
                    print("学员不存在！")
                    continue
                else:
                    get_obj_list(file_name)
        elif choice == "2":
            while True:
                name = input("输入要注册学员的姓名:").strip()
                School.get_all_obj_list()
                kc = input("输入要学习的课程名：").strip()
                if kc.lower() == "python" or kc.lower() == "linux" or kc.lower() == "go":
                    st = Student(name, kc.lower())
                    st.save()
                    break
                else:
                    print("课程不存在！")
                    continue
        elif choice == "3":
            break
        else:
            continue


def teacher():
    pass

def admin():
    pass



def login():
    while True:
        print('''
        1.学生平台（实现）
        2.教师平台(未实现)
        3.管理员平台（未实现）
        4.退出
        ''')
        menu_dic = {
            "1": student,
            "2": teacher,
            "3": admin,
            "4": exit
        }
        choice = input('请输入您要选择的操作：').strip()
        if len(choice) == 0 or choice not in menu_dic:continue
        if choice == "4":break
        menu_dic[choice]()

bkecheng = [Course('python', 10000, "8个月"), Course('linux', 15000, "9个月")]
bteacher = [Teacher('alex', "s1", "老男孩"), Teacher('egon', "s1", "老男孩")]
s1 = School('老男孩', '北京', bkecheng, bteacher)
s1.save()

skecheng = [Course('go', 7000, "7个月")]
steacher = [Teacher('rain', "s1", "北大青鸟")]
s2 = School('北大青鸟', '上海', skecheng, steacher)
s2.save()

if __name__ == "__main__":
    login()


