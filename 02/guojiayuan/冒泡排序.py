list = [9, 102, 14, 24, 44, 23, 55, 2, 20]
for time in range(len(list)):
	for num in range(len(list) - 1):
		if list[num] > list[num + 1]:
			tmp = list[num]
			list[num] = list[num + 1]
			list[num + 1] = tmp
	print([list])
	print('第', time + 1, '轮可得到', len(list) - time, '位的最大值')