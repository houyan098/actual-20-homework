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
