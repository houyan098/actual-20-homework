#coding:utf-8

import random
count = 0
random_num = random.randint(0,100)
while count < 5:
	input_num = int(input('请输入你的数字: '))

	if input_num < random_num:
		print('猜小了')
	elif input_num > random_num:
		print('猜大了')
	else:
		print('猜对了')
		break
	count += 1

	if count == 5:
		print('太笨了，下次再来')
		break


'''
批注: 5

改进点：
1. 代码优化，减少重复代码的使用（提取到公共地方）, 比如count判断
'''
