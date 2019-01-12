#coding:utf-8

students = [
    {'id':1, 'name':'kk', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':2, 'name':'薛刚强','sex': '男', 'age':30, 'telphone':'15211110000','address':'西安市'},
    {'id':3, 'name':'高嘉伟', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':4, 'name':'张争光', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':5, 'name':'郭佳媛', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
]

idx = 0

for index,student in enumerate(students):
	if idx < index:
		idx = index 
idx = idx + 1

print('当前用户的编号:', idx + 1)

_id = input('请输入你的id：' )
name = input('请输入姓名: ')
sex = input('请输入性别(男/女):')
age = input('请输入年龄:')
telephone = input('请输入电话号码:')
address = input('请输入家庭住址：')

student = {'_id':_id, 'name':name,'sex': sex, 'age':int(age), 'telephone':telephone,'address': address}
print('当前学生信息:', student)

students.append(student)

print('所有学生信息:', students)














