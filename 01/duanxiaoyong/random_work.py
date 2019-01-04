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
    else:
        print('抱歉！你猜小了！你重新猜测！')

    count +=1

print('太笨了！下次再来吧！')


'''
批注: 1

错误点:
1. 5次内猜测成功, 24行错误提示

优点:
1. 预习和查找range和字符串格式化方法

改进点:
1. 输出内容格式化
2. 考虑将重复代码(多处相同含义代码)优化, 调整代码格式, 比如count递增
3. 较少continue不必要使用, 考虑代码中是否有必要

'''