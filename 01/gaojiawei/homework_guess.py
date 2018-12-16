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