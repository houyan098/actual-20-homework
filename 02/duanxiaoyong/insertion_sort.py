#encoding: utf-8
# Author:duanxiaoyong
# Python 3.6

Number_list = [1,11,22,33,55,23,15,17,29]
#遍历的次数
for i in range(len(Number_list)-1):
    #这个循环负责设置冒泡排序进行的次数
    for j in range(len(Number_list) - i - 1):
        if Number_list[j] > Number_list[j + 1]:
            Number_list[j], Number_list[j + 1] = Number_list[j + 1], Number_list[j]

print(Number_list)



'''
批注: 2

优点：
1. 自己学习a, b = b, a交换元素的方法

改进点:
1. 代码为冒泡排序，并非插入排序
'''
