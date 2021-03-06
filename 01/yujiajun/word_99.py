#用for实现乘法口诀表
#2018/12/22

for line in range(1,10):   #列元素
    for row in range(1,line+1,1):   #行元素
        print(' ',row,'*',line,'=',line*row,end=(' '))  #结尾用空格阻断
        if(row == line ):   #遇到列数等于行数是不输出，改为换行
            print('\n')

'''
批注: 3.5

优点:
1. 预习和查找range和字符串格式化方法
2. 逻辑清晰, 能考虑到直接使用range(1, line+1)来决定每行截止，逻辑思路不错

改进点:
1. 整体代码保证一致性，注意空格使用, 函数调用参数逗号后保留一个空格，算数运算符前后保留一个空格,格式化代码
2. 测试print()和print('\n')的差异
3. 避免不必要的(), 比如end=(''), if(row == line):
加油
'''