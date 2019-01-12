#coding:utf-8

students = [
    {'id':1, 'name':'kk', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':2, 'name':'薛刚强','sex': '男', 'age':30, 'telphone':'15211110000','address':'西安市'},
    {'id':3, 'name':'高嘉伟', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':4, 'name':'张争光', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':5, 'name':'郭佳媛', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
]
student = None
idx = int(input('请输入需要修改的用户编号信息: '))
for index,student in enumerate(students):
	if idx == index:
		print('需要修改的用户信息是: %s' %(students[idx]))
		student = students[idx]
		_input = input('确认需要修改用户的信息吗:y/n: ')
		if _input == 'y':
			_id = input('请输入你的id：' )
			name = input('请输入姓名: ')
			sex = input('请输入性别(男/女):')
			age = input('请输入年龄:')
			telephone = input('请输入电话号码:')
			address = input('请输入家庭住址：')

			student['id'] = _id
			student['name'] = name
			student['sex'] = sex
			student['age'] = age
			student['telephone'] = telephone
			student['address'] = address

print('所有学生信息:', students)



'''
批注: 7

改进点:
1. 注意保持数据类型一致性
'''
