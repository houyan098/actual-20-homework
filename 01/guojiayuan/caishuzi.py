n = 0
import random
random_num = random.randint(0, 100)
a = random_num
while True:
	b = input('请输入数字')
	ib = int(b)
	n += 1
	if ib == a:
		print('猜对了')
		break
	if a > ib:
		print('猜小了')
	if a < ib:
		print('猜大了')
	if n == 5:
		print('太笨了')
		break
