#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)

from conf import my_msg
from bin import control

if __name__ == '__main__':
    control.mysql_login(my_msg.host,my_msg.port,my_msg.user,my_msg.password,my_msg.database)



