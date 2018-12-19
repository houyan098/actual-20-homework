#-第一次作业
'''
a={}
b={}
for x in range(1,5):
    for y in range(1,5):
        b[y]=x*y
    # f=open('dict','w+')
    # a=json.load(f)
    a[x]=b
    # f.write(a)
    # json.dump(a,f)
print(a)
吐血！！！
错误1：多级字典在循环插入key与value时，子字典变化时原字典也变。
根音：引用的子字典为内存地址，子字典变化，原字典会跟着变化。
错误2：在序列化和反序列化时，如果反序列化字典为空会提示错误！
'''
import json
#--------序列化验证
# f=open('dic','w')
# a={1:'zhang',2:'fei'}
# json.dump(a,f)
# f.close()

#--------反序列化验证
# f=open('dic','r')
# a=json.load(f)
# print(type(a),a)

# fuck!!!!!!!!!!!!!!!!!!验证不带子字典就不会变
# a={1:'zhang',2:'zheng'}
# while True:
#     x=int(input())
#     y=x+1
#     a[x]=y
#     print(a)


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

for x in range(1,10):
    for y in range(x,10):   #前面都是重复的，截断前面的
        print("%sx%s=%s "%(x,y,x*y),end='')
        if y==9:   #在 x*到y最后一个数即9的时候进行换行
            print('\n')

for x in range(1,10):
    for k in range(1,x):    #循环打印一段空格来填充让其错位，而且放在这里，x循环才打印
        print(end='    ')
    for y in range(x,10):

        print(x,y,x*y,end='')
        if y == 9:
            print("\n")
#=====>还有一种从上到下，右对齐的打法，后面复习再次写出
# ----------------作业二：-----------
import random
count=0
while count<5:
    random_num = random.randint(0, 100)
    usr_input=int(input("你猜！猜对了我嫁给你！"))
    if usr_input > random_num:
        print("呵呵，你想多了！少猜点")

    elif usr_input < random_num:
        print("穷限制了你的想象！多猜点")
    else:
        print("兄弟你可以去买彩票了！嫁给你是不存在的！")
        break
    count+=1
    if count == 5:
        agin=input("菜鸡!再给你一次机会？（y/n):")
        if agin == 'y':
            count=0
        else:
            break
