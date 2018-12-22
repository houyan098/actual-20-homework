#encoding: utf-8

'''
乘法口诀表
'''

'''
方法1:
'''
row = 1
max_num = 10

while row < max_num:
    col = 1
    while col <= row:
        print(str(col) + '*' + str(row) + '=' + str(col * row), end='\t')
        col += 1
    row += 1
    print()


print('=' * 20)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for row in nums:
    for col in nums:
        if col > row:
            break
        print(str(col) + '*' + str(row) + '=' + str(col * row), end='\t')
    print()
