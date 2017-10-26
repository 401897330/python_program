#!/usr/bin/env python
#-*- coding:utf-8 -*-

def fetch(data):
    with open('haproxy','r',encoding='utf-8') as f:
        data1 = f.readlines()
    for line in data1:
        if data in line:
            start_index = data1.index(line)
            data2 = data1[start_index+1:]
            data2.remove('\n')
            data2.remove('\t\n')
            end_index = None
            for LINE in data2:
                if len(LINE.split(' ')[0]) != 0:
                    end_index = data1.index(LINE)
                    break
            print(end_index)
            data3 = data1[start_index:end_index]
            for i in data3:
                if i != '\n':
                    print(i,end='')

def zeng(data):
    try:
        data = eval(data)
        servername = data['backend']
        ip = data['record']['server']
        weight = str(data['record']['weight'])
        maxconn = str(data['record']['maxconn'])
        if len(servername) == 0 or len(ip) == 0 or len(weight) == 0 or maxconn == 0:
            print("输入内容不能为空！")
        else:
            with open('haproxy', 'a', encoding='utf-8') as f:
                f.write('backend %s\n    server %s weight %s maxconn %s'% (servername,ip,weight,maxconn))
    except NameError :
        print('输入内容格式不对！')

def shan(data):
    with open('haproxy','r',encoding='utf-8') as f:
        data1 = f.readlines()
    for line in data1:
        if data in line:
            start_index = data1.index(line)
            data2 = data1[start_index+1:]
            end_index = start_index + len(data2) + 1
            for line2 in data2:
                if len(line2.split(' ')[0]) != 0 and line2 != '\n':
                    end_index = data1.index(line2)
                    break
            data4 = data1[:start_index]
            data3 = data1[end_index:]
            with open('haproxy','w',encoding='utf-8') as f1:
                for i in data4:
                    f1.write(i)
            with open('haproxy', 'a', encoding='utf-8') as f2:
                for j in data3:
                    f2.write(j)
            break

if __name__ == '__main__':
    msg = '''
        1.查询
        2.添加
        3.删除
        4.退出
    '''

    menu_dic = {
        '1':fetch,
        '2':zeng,
        '3':shan,
        '4':exit
    }

    while True:
        print(msg)
        choice = input('选项>>>').strip()
        if len(choice) == 0 or choice not in menu_dic:continue
        if choice == '4':break
        data = input('数据(删除和查询都是输入域名)>>').strip()
        if len(data) == 0:
            pass
        else:
            menu_dic[choice](data)










