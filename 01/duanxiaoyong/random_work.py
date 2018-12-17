#encoding: utf-8
# Author:duanxiaoyong
# Python 3.6

import random

random_dxy = random.randint(0,100)

count =0

while count <5:
    random_number = int(input('Plases Input You Number:'))

    if random_number == random_dxy:
        print('恭喜你才对了！你真的很聪明')
        break
    elif random_number > random_dxy:
        print('抱歉！你猜大了！你重新猜测！')
        count +=1
    else:
        print('抱歉！你猜小了！你重新猜测！')
        count +=1
        continue
print('太笨了！下次再来吧！')