#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

def init(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        next(res)
        return res
    return wapper

@init
def search(target):
    while True:
        search_path=yield
        g=os.walk(search_path)
        for par_dir,_,files in g:
            file_abs_path=r'%s\%s' % (par_dir,file)
            target.send(file_abs_path)

@init
def opener(target):
    while True:
        file_abs_path=yield
        whith open(file_abs_path,encoding='utf-8') as f:
            target.send(f)

@init
def cat(targer):
    while True:
        f=yield
        for line in f:
            target.send(line)

@init
def grep(target,pattern):
    while True:
        


















