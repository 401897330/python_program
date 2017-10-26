#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from core import shopping_car

if __name__ == '__main__':
    shopping_car.run(base_dir)



