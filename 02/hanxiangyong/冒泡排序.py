#encoding utf-8
num = [6,11,7,9,4,2,1]
count = len(num)-1
for j in range(len(num)-1):
	print('第{0}次循环'.format(j+1))
	for i in range(count):
		if num[i] > num[i+1]:
			num[i],num[i+1] = num[i+1],num[i]
		print(num)
	count = count-1



'''
批注： 3.5
1. 代码逻辑和运行结果正确
2. 自学a, b = b, a交换元素的方式
3. 观察学习到冒泡排序每次可以少比较一次，使用count = count -1进行计数，提高性能

改进点：
1. 逻辑可以再清晰，可以考虑count, j, len(num)的关系
'''