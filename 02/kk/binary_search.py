#encoding: utf-8

nums = [8, 7, 6, 9, 1]

# 分别测试5, 6, 9
find_num = 9
find_index = -1

#二分查找需要保证元素有序，排序
nums.sort()


start = 0
end = len(nums) - 1

while start <= end:
    middle = (start + end) // 2     #计算区间内中间元素索引
    #根据中间元素大小判断查找元素在区间前半段还是后半段

    if find_num == nums[middle]:  #找到了元素
        find_index = middle
        break
    elif find_num > nums[middle]: #在后半段, 修改区间大小, 开始位置为 middle + 1
        start = middle + 1
    else:                         #在前半段, 修改区间大小, 截止位置为 middle - 1
        end = middle - 1



if find_index == -1:
    print('元素 ', find_num, ' 不在列表 ', nums, ' 中')
else:
    print('元素 ', find_num, ' 在列表 ', nums, ' 中')