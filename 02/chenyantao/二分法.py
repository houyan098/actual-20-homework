lst = [5, 13, 19, 21, 37, 56, 64, 75, 80, 88, 92]
print(lst)
head = (0)
tail = int(len(lst))
l = int(len(lst))
i = int(input("请输入你选择的数字: "))
k = lst[l // 2]
while i != k:
    if i < k:
        tail -= l // 2
    elif i > k:
        head += l // 2
    k = lst[(head + tail) // 2]
    l = l // 2
print("您选择的数字排在第",lst.index(i) + 1,"位。")





