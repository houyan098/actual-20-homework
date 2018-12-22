import random
count = 0
num = random.randint(1,100)
while True:
    guess = int(input('请输入猜的数字，输入5次程序退出:'))
    count += 1
    if num == guess:
        print('猜对了,程序退出')
        exit()
    elif count > 4:
        print(f'已超过5次，程序退出！随机数是{num}')
        exit()
    elif guess < num:
        print(f'猜小了,当前已猜{count}次')
    else:
        print(f'猜大了,当前已猜{count}次')

'''
批注: 5

优点:
1. 预习和查找f字符串和exit函数使用
2. 变量命名规范

改进点:
1. 注意exit和break区别
2. 注意空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码
'''