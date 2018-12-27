# <p align='center'>  python序列-课后总结 </p>
    ![](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1545920904113&di=6238d16a7033fcf99c3c514fdf5f097a&imgtype=0&src=http%3A%2F%2Fwx4.sinaimg.cn%2Forj360%2F006xpDOjgy1fxnhqsr2dhj30j60dyaak.jpg)
列表（list）
-
#### list的特点
    1.有序
    2.编号，可以通过编号访问
    3.可遍历
    4.可追加/可插入
    5.可删除/可以弹出
    6.可修改
    7.长度不定

#### list的定义：
    1.使用中括号包含
    2.每个元素之间使用逗号分隔
    3.可包含任意数据类型
    

#### 访问list
    1.列表是有序的数据集，通过列表名[索引]的方式访问列表中的元素
    2.索引编号
    3.从左向右依次为0，1，2，3，…，n – 1
    4.从右向左一次为-1，-2，-3，…，-n
    5.访问元素的索引必须存在，否则报错
    6.元素修改
    7.通过直接给 列表名[索引] 修改对应索引位置的值 
    8.修改元素的索引必须存在，否则报错
    9.删除 del
    
    
#### 使用for访问列表中所有的元素
    1.类型转换
    2.可以通过函数list将其他可遍历的类型转化为列表
    3.使用range函数快速创建序列
    4.range(end) 创建从0到end-1的连续整数组成的序列
    5.range(start, end) 创建从start到end-1的连续整数组成的序列
    6.range(start, end, step)创建从start到end-1的每间隔stop个整数组成的序列
    
#### 列表常见操作
##### 1.获取list元素的数量
```python
>>> nums = [1,2,3,True,False,['a','b','c'],'zhangsan']
>>> len(nums)
7
```
##### 2.获取list中元素最大值、最小值
```python
最大值：max
>>> max_l1 = [1,22,33,44,3,4,5]
>>> max(max_l1)
44

获取list中元素的最小值：
>>> max_l1 = [1,22,33,44,3,4,5]
>>> min(max_l1)
1
```
#####3.判断元素是否在list中存储
```python
>>> l1
[1, 22, 11, 13, 12, 14]
>>> 1 in l1
True
>>> 10 not in l1
True
```
##### 4.根据索引删除list中对应元素
```python
>>> l1
[1, 22, 11, 13, 12, 14]
>>>
>>> del l1[2]   
>>> l1
[1, 22, 13, 12, 14]
```
#### 列表运算

* 四则运算
    - 加(+)
    - 必须为两个list相加
    - 乘(*)
    - 必须一个为整数
* 练习：
```python
>>> l1 = [1,2,3]
>>> l2 = [4,5,6]
>>> l1 + l2
[1, 2, 3, 4, 5, 6]
>>> l1 *3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> l2 *2
[4, 5, 6, 4, 5, 6]
```    
#### 按照规则获取list中一部分元素生成新的list
    list[start:end:step]
    list[::step]
    list[start:end]
    list[:end]
    list[start:]
    list[:]
切片的应用
-
* 复制数组
```python
>>> num=list(range(10))
>>> num
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nums_1 =num
>>> nums_1[1]=20
>>> num
[0, 20, 2, 3, 4, 5, 6, 7, 8, 9]
>>> id(num)
140243791733960 用id(num)表示内存地址
```
* 反转
```python
>>> n1
[0, 20, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> n1[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 20, 0]
```
* 获取索引为偶数的元素组成的list
```python
>>> n1[::2]
[0, 2, 4, 6, 8]
```
* 获取索引为奇数的元素组成的list
```python
>>> n1
[0, 20, 2, 3, 4, 5, 6, 7, 8, 9]
>>> n1[::3]
[0, 3, 6, 9]
```
#### 列表函数

- append 添加元素到list最右侧
- clear 清空list中的元素
- copy 复制list中的所有元素到新list中并返回
- count 计算list中存在相同元素的数量
- extend 将一个可遍历数据中的所有元素追加到list后
- index 获取元素在list中的位置
- insert 在list指定位置添加元素
- pop 弹出list中指定位置的元素（默认最右侧）
- remove 移除list中指定的元素
- reverse对list中元素进行反转
- sort 对list中元素进行排序

##帮助函数
```python
>>> dir(list())
['__add__', '__class__', '__contains__', 
'__delattr__', '__delitem__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__gt__',
'__hash__', '__iadd__', '__imul__', '__init__',
'__init_subclass__', '__iter__', '__le__', 
'__len__', '__lt__', '__mul__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__reversed__', '__rmul__',
'__setattr__', '__setitem__', '__sizeof__',
'__str__', '__subclasshook__', 'append', 
'clear', 'copy', 'count', 'extend', 'index', 
'insert', 'pop', 'remove', 'reverse', 'sort']
```
* 查看函数使用方法

```python
>>> help(list.append)
Help on method_descriptor:

append(...)
L.append(object) -> None -- append object to end
```
** **

函数：append 、 extend
=
描述|append|extend
:---:|:---:|:---:
参数类型|任意类型|可遍历
返回值|无|无
功能|将参数中元素整体追加到list最右侧|将可遍历参数中的每个元素追加到list最右侧

* append

```python
>>> nums
[1, 'zhangsan', [2, 3, 4]]
>>> nums.append('dxy')
>>> nums.append([1,23,4,[1,2,3]])
>>> nums
[1, 'zhangsan', [2, 3, 4], 'dxy', [1, 23, 4, [1, 2, 3]]]
```
* extend
```python
>>> nums
[1, 'zhangsan', [2, 3, 4]]
>>> nums.append('dxy')
>>> nums.append([1,23,4,[1,2,3]])
>>> nums
[1, 'zhangsan', [2, 3, 4], 'dxy', [1, 23, 4, [1, 2, 3]]]
```
** **
函数：Clear 、copy
=
描述|clear|copy
:---:|:---:|:---:
参数类型|无|无
返回值|无|list
功能|清空list|赋值list的元素并返回

- clear
```python
>>> nums
[1, 'zhangsan', [2, 3, 4], 'dxy', [1, 23, 4, [1, 2, 3]]]
>>> nums.clear()
>>> nums
[]
```
- copy
```python
>>> nums = [1,2,3,4,5]
>>> nums_1 = nums.copy()
>>> nums_1
[1, 2, 3, 4, 5]
>>> nums_1[2] = 100
>>> nums
[1, 2, 3, 4, 5]
>>> nums_1
[1, 2, 100, 4, 5]
```
** **

函数：count、index
=
描述|count|index
:---:|:---:|:---:
参数类型|任意类型|任意类型
返回值|lnt|int
功能|获取元素在list中出现的次数|获取元素在list中的位置，不存在则报错，可指定查找list start和end范围

* count
```python
>>> nums = list(range(10))
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nums.count(3)
1
>>> nums.count(-1)
0
```
** **
* index
```python
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nums.index(4)
4
>>> nums.index(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: -1 is not in list
>>> nums.index(2)
2
>>> nums.index(6)
6
```
** **

函数：pop、remove
=
描述|pop|remove
:---:|:---:|:---:
参数类型|整数|任意
返回值|任意|无
功能|根据索引删除list中元素，并返回，若索引在list中不存在则报错|从list中删除指定的值，若值不存在，则报错

* pop
```python
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nums.pop()
9
>>> nums.pop()
8
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7]
>>> nums.pop(3)
3
>>> nums.pop(5)
6
>>> nums
[0, 1, 2, 4, 5, 7]
```
** **
*  remove
```python
>>> nums = [1,2,3,4,5,6,7,8]
>>> nums
[1, 2, 3, 4, 5, 6, 7, 8]
>>> nums.remove(4)
>>> nums.remove(8)
>>> nums
[1, 2, 3, 5, 6, 7]
>>>
```
** **
函数 reverse  sort
=
描述|reverse|sort
:---:|:---:|:---:
参数类型|无|排序规则、是否反转
返回值|无|无
功能|对list的元素是否反转|对list中的元素进行排序
** **
- reverse
```python
>>> nums
[1, 2, 3, 5, 6, 7]
>>> nums.reverse()
>>> nums
[7, 6, 5, 3, 2, 1]
```
-  sort
```python
>>> le
[1, 6, 7, 4, 3, 9, 10]
>>> le.sort()
>>> le
[1, 3, 4, 6, 7, 9, 10]
```
* 队列
    - 先进先出
    - list.append + list.pop(0)
* 堆栈
    - 先进后出
    - list.append + list.pop
```python
练习代码:
jobs = []

while True:
    prompt = input('请输入任务名称/do:')
    if prompt == 'do':
        if jobs:
            print('请完成任务:' + jobs.pop(0))
        else:
            print('所有任务已完成，可以放心下班啦')
            break
    else:
        jobs.append(prompt)
        
```
常用函数：len max min sum 
-
    len 显示列表的长度
    max 显示列表的最大值
    min 显示列表的最小值
    sum 显示所有元素的和
    
##元组介绍
 
* 不可变的列表                          
* 定义                            
* 使用小括号包含                         
* 每个元素之间使用逗号分隔                    
* 可包含任意数据类型                       
* 如果元组只有一个元素时，元素后的逗号不能省略          

元组与列表相同的操作： 
-                    
* 使用方括号加下标访问元素                 
* 切片（形成新元组对象）                  
* count()/index()              
* len()/max()/min()/tuple()    
** **
元组中不允许的操作:                                    
-                                                           
* 修改、新增元素                                                   
* 删除某个元素（但可以删除整个元组）                                         
* 所有会对元组内部元素发生修改动作的方法。例如，元组没有remove，append，pop等方法。          

访问与修改元组
-
-   访问
- 元组是有序的数据集，通过元组名[索引]的方式访问元组中的元素
- 索引编号
- 从左向右依次为0，1，2，3，…，n – 1
- 从右向左一次为-1，-2，-3，…，-n
- 访问元素的索引必须存在，否则报错
- 元素不能修改

元组的四则运算
- 

- 加(+)
    - 必须为两个tuple相加
- 乘(*)
    - 必须一个为整数
```python
练习:
>>> (1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
>>> (1,2,3)*2
(1, 2, 3, 1, 2, 3)
```
** **

python表达式|结果|描述
:---:|:---:|:---:
len(1,2,3)|3|计算元素的长度
(1,2,3)+(4,5,6)|(1,2,3,4,5,6)|相加-连接
('Hi!',)*4|('H!,',('H!,',('H!,',('H!,')|复制
3 in(1,2,3)|True|元素是否存在
for x in(1,2,3):print(x)|123|遍历

** **

遍历元组
-
- 使用for访问元组中所有的元素
- 类型转换
- 可以通过函数tuple将其他可遍历的类型转化为元组
```python
>>> tuple(range(10))
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```
元组常见操作
-
- 获取tuple元素的数量
- 获取tuple中元素最大值、最小值
- 判断元素是否在tuple中存储
```python
>>> nums
(1, 2, 3, 4, 5)
>>> len(nums)
5
>>> max(nums)
5
>>> 2 in nums
True
>>> 10 not in nums
True
```
元组的四则运算
-
- 加(+)
    - 必须为两个tuple相加
- 乘(*)
    - 必须一个为整数
```python
>>> t1 = (1,2,3)
>>> t2 = (4,5,6)
>>> t1 + t2
(1, 2, 3, 4, 5, 6)
>>> t1 *2
(1, 2, 3, 1, 2, 3)

```
元组的切片
-
- 按照规则获取tuple中一部分元素生成新的tuple
    - tuple[start:end:step]
    - tuple [::step]
    - tuple[start:end]
    - tuple[:end]
    - tuple [start:]
    - tuple[:]
```python
>>> nums = tuple(range(10))
>>> nums
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> nums[:3]
(0, 1, 2)
>>> nums[4:7]
(4, 5, 6)
>>> nums[4:7:2]
(4, 6)
```

元组的不可变性
- 
*  不可变指的是元组的内元素的值不可变                          
* 对于list等复杂数据类型的为引用方式存储数据类型的地址，其地址不可变，但内部数据可变
* count 计算tuple中存在相同元素的数量                    
* index 获取元素在tuple中的位置                       
* split 分割    
* 元组只保证它的一级子元素不可变，对于嵌套的元素内部，不保证不可变！ 
```python
>>> tup = ('a', 'b', ['A', 'B'])
>>> tup[2][0] = 'X'
>>> tup[2][1] = 'Y'
>>> tup 
('a', 'b', ['X', 'Y'])
```
** **
```python
>>> l1
(1, 2, [5, 6])
>>>
>>>
>>> l1[2]
[5, 6]
>>> l1[2] = [11,22,33]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
** **

元组函数
-
count 计算tuple中存在相同元素的数量
index 获取元素在tuple中的位置

```python
>>> dir(tuple)
['__add__', '__class__', 
'__contains__', '__delattr__',
 '__dir__', '__doc__', '__eq__', 
 '__format__', '__ge__', '__getattribute__', 
 '__getitem__', '__getnewargs__', '__gt__', 
 '__hash__', '__init__', '__init_subclass__',
  '__iter__', '__le__', '__len__', '__lt__', 
  '__mul__', '__ne__', '__new__', 
  '__reduce__', '__reduce_ex__', 
  '__repr__', '__rmul__', '__setattr__',
  '__sizeof__', '__str__', '__subclasshook__',
   'count', 'index']
```
课堂练习
-
- 找出 nums=[6, 11, 7, 9, 4, 2, 1]中最大的数字
- 移动nums中最大的数字到最后
** **
* 从右到左依次两两比较，如果前面比后面大，则交换位置
* 第1次: 6，11比较，前面小，不交换[6, 11, 7, 9, 4, 2, 1]
* 第2次: 11, 7比较，前面大，交换[6, 7, 11, 9, 4, 2, 1]
* 第3次: 11, 9比较，前面大，交换[6, 7, 9, 11, 4, 2, 1]
* 第4次: 11, 4比较，前面大，交换[6, 7, 9, 4, 11, 2, 1]
* 第5次: 11, 2比较，前面大，交换[6, 7, 9, 4, 2, 11, 1]
* 第6次: 11, 1比较，前面大，交换[6, 7, 9, 4, 2, 1, 11]
* 交换元素
* tmp = a; a=b; b = tmp;
* a, b = b, a
** **
```python
nums=[6, 11, 7, 9, 4, 2, 1]

for i in range(len(nums)-1):
    for idx in range(len(nums)-1):
        if nums[idx] > nums[idx +1]:
            tmp = nums[idx]
            nums[idx] = nums[idx + 1]
            nums[idx +1] = tmp
print(nums)
```
练习2
- 

* 获取两个list中相同的元素到第三个列表中
* nums_1 = [1, 2, 3, 4, 5, 3, 10, 11]
* nums_2 = [1, 2, 3, 1, 4, 5, 5, 3, 12, 34]
* 保证第二个练习中第三个列表中元素不重复

```python
nums1 = [1,2,3,4,5,3,10,11]
nums2 = [1,2,3,1,4,5,5,3,12,24]
nums3 = []

for i in nums1:
    if i in nums2 and i not in nums3:
        nums3.append(i)
print(nums3)
```

None
-
* None 表示什么都没有
* python中None代表一个特殊的空值，即为一个空对象，没有任何的值
* 练习中 None 解决nums负值的问题
```python
nums = [-1,-2,-3,-4,11,22]

first_num = None
for num  in nums:
    if first_num is  None:
        first_num = num
    elif num > first_num:
        first_num = num
print(first_num)
```
