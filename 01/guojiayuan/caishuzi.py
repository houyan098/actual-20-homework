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

'''
批注: 4

优点:
1. 代码写的简洁、工整

改进点:
1. 导入放在代码最上面（模块时会讲解）
2. 避免不必要的变量，比如a
3. 尝试使用if elseif else语法
4. 注意代码中tab键的使用，配置编辑器使用四个空格替代

加油，第一次写代码，逻辑最重要，正确性其次，好好加油
'''