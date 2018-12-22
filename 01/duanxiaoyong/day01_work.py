#encoding: utf-8
# Author:duanxiaoyong
# Python 3.6

for i in  range(1,10):
    for j  in range(1,i+1):
        if i ==j:
            print(str(j) + "*" + str(i), "=",i *j)
        else:
            print(str(j) + "*" + str(i), "=",i * j, end="")


'''
批注: 3

优点:
1. 预习和查找range和字符串格式化方法

改进点:
1. 输出内容格式化
2. 注意空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码
3. 代码优化, 重复冗余代码优化, 两次print内容
'''
