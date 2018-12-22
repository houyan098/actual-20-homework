# coding:utf-8

# 循环次数
for i in range(1,10):
	# 每次循环乘法次数
	for cnt in range(1,i+1):
		# 格式化间距，省略末尾回车
		print('%s * %s = %-3s' %(cnt,i,cnt*i),end=' ')
	# 每次循环后回车
	print('')


'''
批注: 8

优点:
1. 预习和查找range和字符串格式化方法
2. 逻辑和注释清晰

改进点:
1. 脚本名称, 使用python变量命名规范
2. 注意空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码

'''