#!/usr/bin/python
a = [1,6,4,10,19,3,7]

for j in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i] > a[i+1]:
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
print(a)
