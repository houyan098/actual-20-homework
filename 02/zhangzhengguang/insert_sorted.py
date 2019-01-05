#!/usr/bin/python3
#Author:zhangzhengguang
# -*- coding: utf-8 -*-
# @Time   :2018/12/29 17:56
list_ = sorted([3,6,13,17,24,27,33,38,44,57,60,71,84,99])

num = input('Please input a number:')
if num.isnumeric() and int(num) not in list_:
    list_.append(int(num))
    for i in range(len(list_)):
        if list_[i] > list_[len(list_)-1]:
            '''一旦发现i对应的值大于输入的数时，把i对应的值与输入的数调换
            调换后，后面随着i增加，继续与最后一个相比把较小的数往前排即可'''
            list_[i],list_[len(list_)-1] = list_[len(list_)-1],list_[i]
    print(list_)
else:
    print('Please input a number or entered is already in the list!')


'''
批注： 2
1. 插入逻辑正确，但是并非为插入排序

'''