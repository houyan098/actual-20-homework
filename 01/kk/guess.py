#encoding: utf-8

import random

max_guess_count = 5
random_guess = random.randint(0, 100)
guess_count = 1

while True:
    txt_guess = input('请猜数:')
    num_guess = int(txt_guess)

    if num_guess == random_guess:
        print('猜对了')
        break
    elif num_guess > random_guess:
        print('猜大了')
    else:
        print('猜小了')

    guess_count += 1
    if guess_count > max_guess_count:
        print('游戏结束，正确答案为:', random_guess)
        break