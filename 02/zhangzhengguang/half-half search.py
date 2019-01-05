#!/usr/bin/python3
#Author:zhangzhengguang
# -*- coding: utf-8 -*-
# @Time   :2018/12/26 20:01
list = [1,2,3,4,5,6,7,8,9]
x = 1
guess = 2
mol = 1
'''
使用列表长度系数系数分子mol分母deno与计算次数x相关联的方式，第一次mol取1(twice取2*mol+1or-1)，分母deno一直采用2**x，
当大于guess时下一次分子取2*mol-1，小于guess时下一次分子取2*mol+1
未采用首尾相加折半取值的简洁算法，建议使用首尾相加折中模式简单、好写、不易出错！！！
'''
while True:
    deno = 2**(x)
    '''这里分母deno直接取整会导致分母为0，后面出各种bug，
    应直接分子分母计算完后再取整'''
    if list[int((mol /deno)*len(list))] == guess:
        print("Ok,Find it: %s ,used %s times"%(guess,x))
        break
    elif list[int((mol /deno)*len(list))] > guess:
        mol = 2 * mol - 1
    else:
        mol = 2 * mol + 1
    x+=1


'''
批注： 2.5
1. 逻辑需要再清晰
2. 测试全面，考虑元素存在，也要考虑元素不存在

'''