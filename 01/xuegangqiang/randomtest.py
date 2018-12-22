#encoding: utf8
# xuegqcto@aliyun.com
# python3.6

#===================猜数====================
'''
猜数游戏
随机生成一个0到100的数字，提示用户在控制台上输入一个数字
当用户输入数字小于生成的随机数，则打印猜小了
当用户输入数字大于生成的随机数，则打印猜大了
当用户输入数字等于生成的随机数，则打印猜对了，结束程序
用户最可猜测5次，如果5次都错误，则打印“太笨了，下次再来”，并结束程序
'''

# 生成一个随机数
import random
random_num = random.randint(0, 100)

n = 1
print('本次随机数是:', random_num)

while n <= 5:
    num = input('请输入一个数字:')
    num = int(num)

    if num < random_num:
        print('猜小了')
    elif num > random_num:
        print('猜大了')
    elif num == random_num:
        print('猜对了')
        break
    n += 1

else:
    print('太笨了，下次再来')


'''
批注: 5
优点：
1. 查找while/else语法


改进点：
1. >, =, <三条件可以直接使用if, elif, else逻辑流程
'''
