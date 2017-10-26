#!/usr/bin/env python
#-*- coding:utf-8 -*-

import logging
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def loger(which,user,money,goods):
    logging.basicConfig(filename='%s\logs\%s_access.log'% (base_dir, which),
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)
    if goods == 0:
        logging.debug("user:%s   enchashment:%s" % (user,money))
    else:
        logging.debug("user:%s   goods:%s   balance:%s" % (user, str(goods), money))
