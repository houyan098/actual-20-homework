#coding:utf-8

students = [
    {'id':1, 'name':'kk', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':2, 'name':'薛刚强','sex': '男', 'age':30, 'telphone':'15211110000','address':'西安市'},
    {'id':3, 'name':'高嘉伟', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':4, 'name':'张争光', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
    {'id':5, 'name':'郭佳媛', 'sex':'男', 'age':30, 'telphone':'15200000000', 'address':'西安市'},
]

id_text = int(input('请输入需要查找的学生的id:'))

for idx,student in enumerate(students):
	if idx == id_text:
		print('该学生的信息是 %s' %(students[idx]),)
		break
	else:
		print('没有找到该学生信息')


'''
批注: 7


改进点:
1. 用户编号一般作为唯一标识，但是不会根据其进行查询，一般根据可记忆信息或区分性信息进行查询，比如姓名，年龄，地址，电话号码
'''