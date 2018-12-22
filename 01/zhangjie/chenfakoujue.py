#coding:utf-8

for i in range(1,10):
	for j in range(1,i+1):
		print("%d * %d = %d" % (j,i,i * j),end=" ")
	print(" ")

'''
批注: 3

优点:
1. 预习和查找字符串格式化

改进点:
1. 注意空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码
2. 注意和print(' '), print(''), print() 的区别
'''