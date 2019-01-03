#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auth : xuegqcto@aliyun.com

# 定义一个列表
nums = [11, 9, 22, 5, 30, 28, 15]

# 第一层for 循环用于控制 len(nums)次
for num in nums:

    # 第二次for 循环用于前后比较，最终将列表最大值放到列表的最后。
    # 循环len(nums)次，将变为有顺序的列表
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i],nums[i+1] = nums[i+1], nums[i]

print(nums)

