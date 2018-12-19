#-第一次作业
# a='---------'
# b="|"
# print(a+'\n1 x 1= 1 %s'%b)
# print(a*2+'\n1 x 2= 1 %s2 x 2= 4 %s'%(b,b))
# print(a*3+'\n1 x 3= 3 %s2 x 3= 6 %s3 x 3= 9 %s'%(b,b,b))
#嗯，给我打印100*100的乘法矩阵吧。。。。。换一种方法：

#----------------作业1---------------------
for x in range(1,10):
    for y in range(1,x+1):   #不需要循环y那么多，后面都重复了，到x*x就截断到下一次循环
        print("%sx%s=%s "%(x,y,x*y),end='')
        if x==y:  #在 x*x的这里进行判断换行
            print('\n')
'''
for x in range(1,10):
    for y in range(x,10):   #前面都是重复的，截断前面的
        print("%sx%s=%s "%(x,y,x*y),end='')
        if y==9:   #在 x*到y最后一个数即9的时候进行换行
            print('\n')
'''
'''
for x in range(1,10):
    for k in range(1,x):    #循环打印一段空格来填充让其错位，而且放在这里，x循环才打印
        print(end='    ')
    for y in range(x,10):
        print(x,y,x*y,end='')
        if y == 9:
            print("\n")
'''
#=====>还有一种从上到下，右对齐的打法，后面复习再次写出