#encoding: utf-8
# Author:duanxiaoyong
# Python 3.6

# 二分查找的原理：
# 优点：二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好
# 缺点：缺点是要求待查表为有序表，且插入删除困难
#思路：
# 1.假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，如果两者相等，则查找成功
# 2.否则利用中间位置记录将表分成前、后两个子表
# 3.如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表
# 4.直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。


# 方法1
test_list=[5,13,19,21,37,56,64,75,80,88,92,100,101,199,1000,108,109,122]
test_list.sort()#对列表进行排序，列表是有序的，是二分法的前提
print(test_list)
#定义开始的索引
start=0
#定义结束的索引
end=int(len(test_list)-1)
find_num=int(input('请输入列表中要查找的数字：'))

while True:
    #定义中间索引
    mid=(end+start)//2
    mid_num=test_list[mid]
    if find_num not in test_list:
        print('你查询的数字，列表中不存在')
        break
    if find_num > mid_num:
        start=mid+1
    elif find_num < mid_num:
        end=mid
    else:
        print('你查询的数字的索引值为：{0}'.format(mid))
        break

# 方法2
def binary_list(len_list, find_num):
    # 取中间位数
    mid = int(len(len_list) // 2)

    if len(len_list) >= 1:
        if len_list[mid] > find_num:  # 中间位数大于要查找的数，则要查找的数在左半部分，继续调用二分算法进行查找
            binary_list(len_list[:mid], find_num)
        elif len_list[mid] < find_num:  # 中位数小于要查找的数，则要查找的数在右半部分
            binary_list(len_list[mid:], find_num)
        else:  # 中间位数等于要查找的数
            print("恭喜你，查到了：", len_list[mid])
    else:
        print("抱歉！没有找到")

data=list(range(1,1000))
binary_list(data,999)