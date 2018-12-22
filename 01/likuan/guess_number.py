#!/usr/bin/python
import random

#生成一个随机数0-100
random_num = random.randint(0, 100)
print("生成的随机数是:",random_num)
i = 0
while True:
    num = int(input("请你猜一个数:"))
    if num < random_num :
        print("猜小了请重新猜!")
        i += 1
    elif num > random_num :
        print("猜大了请重新猜!")
        i += 1
    elif num == random_num :
        print("猜对了!退出程序!")
        break
    if i >= 5:
        print("太笨了，猜了5次都猜不对，下次再来，退出程序")
        break



'''
批注: 3

改进点：
1. 考虑将重复代码(多处相同含义代码)优化, 调整代码格式, 比如i递增
2. >, =, <三条件可以直接使用if, elif, else逻辑流程
3. 注意考虑空格使用, while/if后的冒号前一般不保留空格， 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码
'''