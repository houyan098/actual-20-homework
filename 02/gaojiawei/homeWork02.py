#冒泡排序
my_list = [3,6,1,2,7,9,5]
for i in range(len(my_list)-1):
    for j in range(len(my_list)-1):
        if my_list[j] > my_list[j+1]:
            tmp = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = tmp
print(my_list)
#插入排序
my_list_1 = [3,6,1,2,7,9,5]
for i in range(len(my_list_1)):
    for j in range(i,0,-1):
        if my_list_1[j-1] >my_list_1[j]:
            tmp = my_list_1[j-1]
            my_list_1[j-1] = my_list_1[j]
            my_list_1[j] = tmp
print(my_list_1)
#二分查找
my_list_2 = [3,6,1,2,7,9,5]
def func(my_list_2,aim):
    mid = (len(my_list_2)-1)//2
    if my_list_2:
        if aim > my_list_2[mid]:
            func(my_list_2[mid+1:],aim)
        elif aim < my_list_2[mid]:
            func(my_list_2[:mid],aim)
        elif aim == my_list_2[mid]:
            print("找到了",mid)
    else:
        print('找不到')
func(my_list_2,2)
