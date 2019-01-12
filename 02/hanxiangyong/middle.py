#encoding utf-8
num = list(range(0,30,3))
print(num)
goal = int(input('请输入一个0到30之间的数'))
start = 0
end = len(num)-1
while True:
	if start < end:
		#print('a')
		mid = (start + end)//2
		if num[mid] == goal:
			print('要找的数为列表的第{0}个数{1}'.format(mid+1,num[mid]))
			break
		elif goal > num[mid]:
			start = mid + 1
		else:
			end = mid - 1
	else:
		print('输入的数不在列表中')
		break