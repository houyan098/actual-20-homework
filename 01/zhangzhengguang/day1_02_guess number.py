# ----------------作业二：-----------
import random
count = 0
while count < 5:
    random_num = random.randint(0, 100)

    usr_input = int(input("你猜！猜对了我嫁给你！"))

    if usr_input > random_num:
        print("猜小了")
    elif usr_input < random_num:
        print("猜大了")
    else:
        print("兄弟你可以去买彩票了！嫁给你是不存在的！")
        break

    count += 1
    if count == 5:
        agin=input("菜鸡!再给你一次机会？（y/n):")
        if agin == 'y':
            count=0
        else:
            break

'''
批注: 2

错误点:
1. 随机数生成时间，应该在每次游戏开始

优点:
1. 唯一考虑游戏重新开始

改进点：
1. 注意空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码
2. 注意print('\n'), print(''), print()区别
3. 考虑将重复代码(多处相同含义代码)优化, 调整代码格式, 比如count判断
'''
