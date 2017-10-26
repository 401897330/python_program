#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from django import template

register = template.Library()

@register.filter
def order_number(num1, num2):
    return num1+(num2 - 1)*20

@register.filter
def digital(str):
    try:
        return float(str)
    except Exception as e:
        return 1


@register.filter
def compare(num1, num2):
    try:
        if int(num1) < int(num2):
            return 1
        else:
            return 0
    except Exception as e:
        return 1

