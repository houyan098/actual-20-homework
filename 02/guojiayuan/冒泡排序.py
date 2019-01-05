list = [9, 102, 14, 24, 44, 23, 55, 2, 20]
for time in range(len(list)):
	for num in range(len(list) - 1):
		if list[num] > list[num + 1]:
			tmp = list[num]
			list[num] = list[num + 1]
			list[num + 1] = tmp
	print([list])
	print('第', time + 1, '轮可得到', len(list) - time, '位的最大值')

'''
批注： 3.5
1. 思路和流程清晰
2. 笔记做的不错，加油

改进点：
1. list, time为python内置数据类型，避免命名使用（需要逐渐积累）
2. 第8行 list本身为列表，这行代码使用理由


多练习，完成作业插入排序和二分查找
'''