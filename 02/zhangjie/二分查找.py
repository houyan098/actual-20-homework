def search(data_set,value):
	low = 0
	high = len(data_set) - 1

	while low <= high:
		mid = (low+high)//2
		if data_set[mid] == value:
			return mid
		elif data_set[mid] > value:
			high = mid -1
		else:
			low = mid + 1

data_set =  list(range(100))
print(search(data_set,36))


'''
批注： 8
1. 代码思路清晰
2. 使用了函数

'''