#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auth : xuegqcto@aliyun.com

'''
描述：二分查找又称折半查找，它是一种效率较高的查找方法。

二分查找要求：
（1）必须采用顺序存储结构
（2）.必须按关键字大小有序排列

查找过程
首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，
如果两者相等，则查找成功；否则利用中间位置记录将表分成前、后两个子表，
如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。
重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。
'''

# 初始化一个有序列表
nums = list(range(0, 101))

print(nums)

# 计数
count = 0

# 定义索引
idx_min = 0
idx_max = len(nums)-1

txt = input('请输入数字: ')
txt_int = int(txt)

print(idx_min, idx_max)

while idx_min <= idx_max:

    count += 1

    mid = (idx_min + idx_max) // 2

    if  txt_int > nums[mid]:
        idx_min = mid + 1
    elif txt_int < nums[mid]:
        idx_max = mid -1
    else:
        print('恭喜，猜对了', txt_int)
        break

    # 格式化输出，便于理解每次比对情况
    print('第{0}次, idx_min:{1}, mdx_max:{2}，mid:{3}'.format(count, idx_min, idx_max, mid))
