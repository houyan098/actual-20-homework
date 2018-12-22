#encoding: utf8
# xuegqcto@aliyun.com
# python3.6

# 打印乘法口诀表
i = 1
while i <=9:
    j = 1
    while j <= i:
        print(str(j) + '*' + str(i)  + '=' + str(j * i), end=' ')
        j += 1
    print()
    i += 1


'''
批注: 8
优点：
1. 唯一一个使用while完成作业的同学


改进点：
1. 注意考虑空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码
'''
