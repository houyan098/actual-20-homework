#!/usr/bin/python
a = [2,4,3,10,6,8,14,1]
for i in range(1,len(a)):
      x = a[i]
      for j in range(i,-1,-1):
          if x < a[j-1]:
              a[j] = a[j-1]
          else:
              break
      a[j] = x
print(a)


'''
批注： 8.5
1. 思路和流程清晰

改进点：
1. 注意代码风格，使用4个空格
2. 考虑j变量在for之内循环定义，在第10行也有使用，可以考虑下j定义在第一层循环内（代码习惯）

多练习，完成作业插入排序和二分查找
'''