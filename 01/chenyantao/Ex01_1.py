for row in range(1,10):
    for column in range(row,10):
        print(str(row)+"*"+str(column)+"="+str(row * column), end="  ")
    print("")


'''
批注: 5

优点：
1. 使用row, column命名变量，命名规范
2. 预习和查找range用法

改进点:
1. 注意空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码

其他:
1. 可以使用while, for多种方式实现，对比优缺点, 找到最佳代码实现方式

'''