lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in lst[1::]:
    n = lst.index(i)
    while i < lst[n]:
        i, lst[n] = lst[n], i
        n -= 1


'''
批注: 2

改进点:
1. 首先测试代码
2. 考虑5行代码结果

'''
