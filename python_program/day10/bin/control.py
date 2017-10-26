#!/usr/bin/env python
#-*- coding:utf-8 -*-

import paramiko
import pymysql


def run_cmd(result):
    while True:
        cmd = input('输入要执行命令,退出输入"exit">>:')
        if cmd == "exit": break
        for i in result:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(i['IP'], i['port'], i['user'], i['password'])
            stdin, stdout, stderr = ssh.exec_command(cmd)
            print(20 * "*" + i['IP'] + 20 * "*")
            if stderr:
                for err_msg in stderr.readlines():
                    print(err_msg, end='')
            for msg in stdout.readlines():
                print(msg, end='')
        ssh.close()

def ssh_client(result):
    stop = True
    while stop:
        num = input('输入要执行命令的主机号,多台之间用","号分割，全部执行的话输入\033[1;32mall\033[0m:').strip()
        if not num:continue
        if num.lower() == 'exit':break
        if num.lower() == 'all':
            run_cmd(result)
            stop = False
        else:
            result_list = []
            num_list = num.split(",")
            for i in num_list:
                if i.isdigit() and int(i) <= len(result):
                    result_list.append(result[int(i)-1])
                else:
                    print("%s号主机不存在，请重新输入！"% i)
                    break
            if len(num_list) == len(result_list):
                run_cmd(result_list)
                stop = False

def mysql_login(host,port,User,password,database):
    while True:
        user = input('请输入用户名:')
        pwd = input('请输入密码:')
        conn = pymysql.Connect(host=host, port=port, user=User, password=password, database=database,
                               charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('select * from user where user=%s and password=%s', [user, pwd])
        result = cursor.fetchone()
        if result == None:
            print('用户名或密码错误！')
            continue
        cursor.execute('select * from department where id=%s',result['department_id'])
        result2 = cursor.fetchone()
        print('当前登录用户：%s  所属部门为：%s' % (result['user'], result2['dname']))
        cursor.execute('select user.user,machine.IP from user_machine left join user on user_machine.user_id = user.id left join machine on user_machine.machine_id = machine.id where user.user=%s',result['user'])
        result3 = cursor.fetchall()
        if not result3:continue
        print('%s所管理的主机有：'% result['user'])
        for i,msg in enumerate(result3, 1):
            print("\033[1;31m %s \033[0m" % i,msg['IP'])
        cursor.execute('select machine.IP,machine.user,machine.port,machine.password from user_machine left join user on user_machine.user_id = user.id left join machine on user_machine.machine_id = machine.id where user.user=%s',result['user'])
        result4 = cursor.fetchall()
        cursor.close()
        conn.close()
        ssh_client(result4)
        break



