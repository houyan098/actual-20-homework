lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in lst[1::]:
    n = lst.index(i)
    while i < lst[n]:
        i, lst[n] = lst[n], i
        n -= 1






