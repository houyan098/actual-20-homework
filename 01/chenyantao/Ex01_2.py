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
