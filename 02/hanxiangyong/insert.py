#encoding utf-8
num = [6,11,7,9,4,2,1]
for i in range(1,len(num)):
	print('第{0}次循环',{i})
	j = i-1
	for k in range(i+1):
		if j >= 0:
			if num[i] > num[j]:
				num.insert(j+1,num[i])
				num.pop(i+1)
#			print('11')		测试
				break
			else:
				j = j-1
#				print(j)	测试
		else:
			num.insert(0,num[i])
			num.pop(i+1)
#			print('22')		测试
	print(num)
		
		
		
		