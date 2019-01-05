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





'''
批注: 2

改进点:
1. 首先测试代码, 元素存在和元素不存在都要测试到
2. 考虑第8行，在条件在不存在时需要如何优化
3. 考虑15行代码index和代码功能（目前二分查找与index功能类似）

'''
