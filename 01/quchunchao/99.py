for x in range(1,10):
    for y in range(1,10):
        sum = x * y
        print(f'{x} * {y} = {sum}')


'''
批注: 3
优点：
1. 预习和查找f字符串格式化使用(个人不建议使用，数据和操作未分离，在web项目中容易产生安全问题)


改进点：
1. 注意考虑空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码
2. 注意输出格式控制, 三角形和换行
'''