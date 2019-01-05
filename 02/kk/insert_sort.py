#encoding: utf-8


nums = [8, 7, 6, 9, 1]

'''
从索引为1的元素开始, 每次保证前面的n个数字有序

'''

for index in range(1, len(nums)):

    '''
        从排序元素开始向前两两比较，如果前面比后面大，交换
    '''
    for sindex in range(index, 0, -1):
        if nums[sindex - 1] > nums[sindex]:
            temp = nums[sindex]
            nums[sindex] = nums[sindex - 1]
            nums[sindex - 1] = temp


print(nums)