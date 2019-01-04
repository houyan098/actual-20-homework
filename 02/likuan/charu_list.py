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
