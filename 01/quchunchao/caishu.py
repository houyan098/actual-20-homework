#!/usr/bin/python
#enconding utf8
import  random
num = random.randint(0,100)
count = 0

while True:
    sum = int(input('请输入数字：\n'))
    count = count + 1
# 输入次数超过5次退出
    if count >= 5:
        break
    if num == sum:
        print(f'恭喜你猜对了 {num}')
        exit()
    elif sum > num:
        print(f'输入的数字大于随机数 {sum} 当前输入次数{count}')
    elif sum < num:
        print(f'输入的数字小于随机数 {sum} 当前输入次数{count}')
