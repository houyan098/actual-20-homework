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
