#!/usr/bin/env python
#-*- coding:utf-8 -*-

def open_file(file_name):
    with open("%s" % (file_name), "r",encoding='utf-8') as f:
        data = f.readlines()
    data2 = data[0]
    return data2

def Data(file_name):
    with open("%s" % (file_name), "r",encoding='utf-8') as f:
        file = f.readlines()
    return file

def zen():
    file_name = sql.split('into')[1].strip().split(' ')[0].strip()
    msg = sql.split('values')[1].strip()
    if len(msg) == 0:
        print("插入的内容不能为空！")
    else:
        user_msg = msg.split(',')
        if len(user_msg) == 5:
            data2 = Data(file_name)
            num = str(len(data2))
            with open("%s" % (file_name), "a",encoding="utf-8") as f:
                f.write('\n%s,%s' % (num,msg))
            print("insert successful")
        else:
            print("插入字段需为5段(user_name,user_age,tel,work,time)，请重新输入！")

def shan():
    file_name = sql.split('from')[1].strip().split(' ')[0].strip()
    title = open_file(file_name)
    if '<' in sql and '>' not in sql and '=' not in sql:
        num = int(sql.split('where')[1].strip().split('<')[1].strip())
        data = Data(file_name)
        data2 = data[:num]
        with open("%s" % (file_name), "w", encoding='utf-8') as f:
            for i in data2:
                f.write(i)

    elif '>' in sql and '<' not in sql and '=' not in sql:
        num = int(sql.split('where')[1].strip().split('>')[1].strip())
        data = Data(file_name)
        data2 = data[num:]
        with open("%s" % (file_name), "w", encoding='utf-8') as f:
            for i in data2:
                f.write(i)


    elif '=' in sql and '<' not in sql and '>' not in sql:
        num = int(sql.split('where')[1].strip().split('=')[1].strip())
        data = Data(file_name)
        data2 = data[num]
        with open("%s" % (file_name), "w", encoding='utf-8') as f:
            for i in data:
                if i == data2:
                    pass
                else:
                    f.write(i)

    elif '<' in sql and '=' in sql and '>' not in sql:
        num = int(sql.split('where')[1].strip().split('=')[1].strip())
        data = Data(file_name)
        data2 = data[:num+1]
        with open("%s" % (file_name), "w", encoding='utf-8') as f:
            for i in data2:
                f.write(i)

    elif '>' in sql and '=' in sql and '<' not in sql:
        num = int(sql.split('where')[1].strip().split('=')[1].strip())
        data = Data(file_name)
        data2 = data[num+1:]
        with open("%s" % (file_name), "w", encoding='utf-8') as f:
            for i in data2:
                f.write(i)

    elif '>' in sql and '<' in sql and '=' not in sql:
        tiaojian = sql.split('id')[1].strip().split('and')[0].strip()
        if '>' in tiaojian:
            num1 = int(sql.split('id')[1].strip().split('and')[0].strip().split('>')[1].strip())
            num2 = int(sql.split('<')[1].strip())
            data = Data(file_name)
            print(data[num1+1:num2])
        else:
            num1 = int(sql.split('id')[1].strip().split('and')[0].strip().split('<')[1].strip())
            num2 = int(sql.split('>')[1].strip())
            data = Data(file_name)
            print(data[num2+1:num1])
    else:
        print('语法错误！')
        operator = sql.split('where')



def gai():
    file_name = sql.split('from')[1].strip().split(' ')[0].strip()



def cha():
    what_select = sql.split('select')[1].strip().split(' ')[0].strip()
    file_name = sql.split('from')[1].strip().split(' ')[0].strip()
    if "*" in sql:
        if "where" in sql:
            file_name = sql.split('from')[1].strip().split(' ')[0].strip()
            title = open_file(file_name)
            if '<' in sql and '>' not in sql and '=' not in sql:
                num = int(sql.split('where')[1].strip().split('<')[1].strip())
                data = Data(file_name)
                for i,ele in enumerate(data,0):
                    print(i,ele)

            elif '>' in sql and '<' not in sql and '=' not in sql:
                num = int(sql.split('where')[1].strip().split('>')[1].strip())
                data = Data(file_name)
                data2 = data[num + 1:]
                for i,ele in enumerate(data2,0):
                    print(i,ele)

            elif '=' in sql and '<' not in sql and '>' not in sql:
                num = int(sql.split('where')[1].strip().split('=')[1].strip())
                data = Data(file_name)
                data2 = data[num]
                for i,ele in enumerate(data2,0):
                    print(i,ele)


            elif '<' in sql and '=' in sql and '>' not in sql:
                num = int(sql.split('where')[1].strip().split('=')[1].strip())
                data = Data(file_name)
                data2 = data[:num + 1]
                for i,ele in enumerate(data2,0):
                    print(i,ele)

            elif '>' in sql and '=' in sql and '<' not in sql:
                num = int(sql.split('where')[1].strip().split('=')[1].strip())
                data = Data(file_name)
                data2 = data[num:]
                for i,ele in enumerate(data2,0):
                    print(i,ele)

            elif '>' in sql and '<' in sql and '=' not in sql:
                tiaojian = sql.split('id')[1].strip().split('and')[0].strip()
                if '>' in tiaojian:
                    num1 = int(sql.split('id')[1].strip().split('and')[0].strip().split('>')[1].strip())
                    num2 = int(sql.split('<')[1].strip())
                    data = Data(file_name)
                    data2 = data[num1 + 1:num2]
                    for i, ele in enumerate(data2, 0):
                        print(i, ele)
                else:
                    num1 = int(sql.split('id')[1].strip().split('and')[0].strip().split('<')[1].strip())
                    num2 = int(sql.split('>')[1].strip())
                    data = Data(file_name)
                    data2 = data[num2 + 1:num1]
                    for i, ele in enumerate(data2, 0):
                        print(i, ele)
            else:
                print('语法错误！')
                operator = sql.split('where')
        else:
            with open("%s" % (file_name),"r",encoding='utf-8') as f:
                data = f.read()
                for i, ele in enumerate(data, 0):
                    print(i,ele)

while True:
    sql = input('sql>').strip().lower()
    word = sql.split(' ')[0].strip()
    if word == "select":
        cha()
    elif word == "insert":
        zen()
    elif word == "update":
        gai()
    elif word == "delete":
        shan()
    elif word == "":
        pass
    elif word == "exit":
        break
    else:
        print("语法错误！请重新输入。")