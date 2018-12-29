#!/usr/bin/python3
#Author:zhangzhengguang
# -*- coding: utf-8 -*-
# @Time   :2018/12/26 20:01
list = [1,2,3,4,5,6,7,8,9]
x = 1
guess = 2
mol = 1
'''
使用列表系数的分子mol分母deno与计算次数x相关联的方式，第一次mol取2x，deno采用2**x，
当大于guess下次计算原分子*2-1，小于时原分子/2+1
未采用首尾相加折半取值的简洁算法，建议使用首尾相加模式
'''
while True:
    deno = 2**(x)
    '''这里分母deno直接取整会导致分母为0，后面出各种bug，
    这里应该直接分子分母计算完后再取整'''
    if list[int((mol /deno)*len(list))] == guess:
        print("ok,find it:%s,used %s times"%(guess,x))
        break
    elif list[int((mol /deno)*len(list))] > guess:
        mol = 2 * mol - 1
    else:
        mol = 2 * mol + 1
    x+=1
