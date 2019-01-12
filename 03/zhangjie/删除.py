#coding:utf-8

students = [
    {'id':1, 'name':'kk', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':2, 'name':'薛刚强','sex': '男', 'age':30, 'telphone':'15211110000','address':'西安市'},
    {'id':3, 'name':'高嘉伟', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':4, 'name':'张争光', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':5, 'name':'郭佳媛', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
]
student = None
idx = int(input('请输入需要删除的用户编号信息: '))
for index,student in enumerate(students):
	if idx == index:
		print('需要删除的用户信息是: %s' %(students[idx]))
		student = students[idx]
		_input = input('确认需要修改用户的信息吗:y/n: ')
		if _input == 'y':
			del students[idx]

print('所有学生信息:', students)


'''
批注: 7

优点
1. 使用enumerate进行list遍历

改进点:
1. 用户编号作为唯一标识，当用户创建时分配，注意用户编号和用户所在位置没有关系
2. 注意enumerate遍历索引位置从0开始
'''