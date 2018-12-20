#!/usr/bin/env python3
#__*__ encoding:utf-8 __*__
#Author : david_liu

"""
猜数游戏，只能猜五次~
"""
import sys
import random

random_num = random.randint(0,100)

i = 0
while i < 5:
    num = int(input('please input number : '))
    if num == random_num:
        print ("猜对了~~")
        break
    elif num > random_num:
        print ("猜错了~太大~")
        i += 1
    elif num < random_num:
        print ("猜错了~太小~")
        i += 1

print ("真笨~重新来吧~~~")
