# coding:utf-8

# 循环次数
for i in range(1,10):
	# 每次循环乘法次数
	for cnt in range(1,i+1):
		# 格式化间距，省略末尾回车
		print('%s * %s = %-3s' %(cnt,i,cnt*i),end=' ')
	# 每次循环后回车
	print('')