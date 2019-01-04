#!/usr/bin/python
a = [1,3,6,10,33,55,66,68,90,100,110,120,140,150,200,250,300]
guess = 55
y = 0
i = len(a) // 2
while True:
    if a[i] > guess:
        y += 1
        i = i // 2
    elif a[i] < guess:
         i += (len(a) - i) // 2
         y += 1
    elif a[i] == guess:
        print(a[i])
        y +=1
        break
print("总共猜的次数是:",y)
