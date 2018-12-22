#!/usr/bin/python
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j) + str("*") + str(i)+"=" + str(i*j),end="\t")
    print()

'''
批注: 8

优点：
1. 预习和查找range用法
2. 使用print end="\t"对输出格式化

改进点:
1. 注意空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码
2. 字符串本身不需要str格式化处理
'''