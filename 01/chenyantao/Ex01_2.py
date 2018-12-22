countdown = 5
import random
sec = random.randint(0,100)
print(sec)
guess = int(input("系统已自动生成一个0-100的随机整数，请输入你猜的数字："))
while countdown > 0:
    if sec == guess:
        print("恭喜猜对了")
        break
    elif guess > sec:
        guess = int(input("猜大了，请重新输入数字："))
    elif guess < sec:
        guess = int(input("猜小了，请重新输入数字："))
    countdown -= 1
    if countdown == 0:
        print("你太笨啦")


'''
批注: 5

优点:
1. 变量命名见名之意
2. 使用countdown递减方式, 有创意

改进点:
1. 考虑将重复代码(多处相同含义代码)优化, 调整代码格式, 比如input输入,countdown判断
2. >, =, <三条件可以直接使用if, elif, else逻辑流程

'''