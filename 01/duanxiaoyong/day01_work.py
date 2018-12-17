#encoding: utf-8
# Author:duanxiaoyong
# Python 3.6

for i in  range(1,10):
    for j  in range(1,i+1):
        if i ==j:
            print(str(j) + "*" + str(i), "=",i *j)
        else:
            print(str(j) + "*" + str(i), "=",i * j, end="")


