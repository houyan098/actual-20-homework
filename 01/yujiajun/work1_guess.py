#猜数游戏
#2018/12/22



import random
guess_again_count=0
max_guess_count = 5  #最大猜数次数

random_guess = random.randint(0,100)  #随机生成准确值
guess_count=1  #猜测次数，赋初值为1

while guess_count<=max_guess_count:   #如果猜测次数小于最大机会就继续执行
    txt_guess = input('请猜数:')
    num_guess = int(txt_guess)
    blank=' '
    if num_guess == random_guess:   #猜对了就跳出循环
        print('猜对了')
        break
    elif num_guess > random_guess:
        print(blank*4,'猜大了')
    else:
        print(blank*4,'猜小了')
    guess_count += 1      #猜测次数不断更新值
    if  guess_count==max_guess_count:
        print(blank*4,'你失败了')
        guess_again_txt=input('想不想再来一次y/n')
        guess_choice=str(guess_again_txt)
        if(guess_choice=='y'):
            guess_count=0
            guess_again_count += 1
        else:
            break
print(blank*4,'本次游戏结束，正确答案为：',random_guess,'你所用的次数为：',guess_again_count)

'''
批注: 3.5

优点:
1. 考虑到重新玩游戏

改进点:
1. 重新开始游戏，随机数需要重新生成
2. 整体代码保证一致性，注意空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码
3. 避免不必要的(), 比如if(guess_choice=='y')

加油
'''