#用for实现乘法口诀表
#2018/12/22

for line in range(1,10):   #列元素
    for row in range(1,line+1,1):   #行元素
        print(' ',row,'*',line,'=',line*row,end=(' '))  #结尾用空格阻断
        if(row == line ):   #遇到列数等于行数是不输出，改为换行
            print('\n')