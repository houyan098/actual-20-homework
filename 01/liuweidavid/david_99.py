#!/usr/bin/env python3
# __*__ encoding:utf-8 __*__
# Author : david_liu

"""
打印99乘法表
"""

for i in range(1,10):
    for j in range(1,i+1):
        # print ('%d X %d = %2d' %(i,j,i*j))
        print( '%d X %d = %2d' % (i ,j ,i*j) ,end=' ' )
        # end 表示输出对象以什么东西结尾
    print (' ')


'''
批注: 4

优点:
1. 预习和查找range和字符串格式化方法
2. 逻辑清晰, 能考虑到直接使用range(1, i+1)来决定每行截止，逻辑思路不错

改进点:
1. 整体代码保证一致性，注意空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码
2. 测试print(), print(' ')区别

加油
'''