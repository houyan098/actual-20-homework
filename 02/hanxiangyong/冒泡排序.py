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
