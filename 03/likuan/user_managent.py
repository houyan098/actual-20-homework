#!/usr/bin/python

#初始化的用户
students = [
    {'id': 1, 'name' : 'name1', 'sex' : '男', 'age' : 30, 'tel' : '15200000000', 'add' : '西安市'},
    {'id': 2, 'name' : 'name2', 'sex' : '男', 'age' : 24, 'tel' : '15235666777', 'add' : '西安市'},
    {'id': 3, 'name' : 'name3', 'sex' : '男', 'age' : 35, 'tel' : '11346774667', 'add' : '西安市'},
    {'id': 4, 'name' : 'name4', 'sex' : '男', 'age' : 36, 'tel' : '15123456735', 'add' : '西安市'},
]

# 获取用户想进行的操作
action = input("请输入你要进行的操作(query/modify/add/del):")

# 定义判断年纪的函数
def age(arg):
    if not arg >= 18 and arg <= 80:
        print("输入的信息错误!")
        exit()

# query 函数
def user_query():
    query = input("请输入你想查询的内容:")
    for student in students:
        if query in [str(student['id']),student['name'],student['sex'],str(student['age']),str(student['add'])]:
            print(student)
        else:
            print("输入的查询内容不存在!")

# modify函数
def user_modify():
    search_id = int(input("请输入修改学生编号:"))
    # i用来判断有没有做修改操作
    i = 0
    for student in students:
        if student['id'] == search_id:
            print("当前用户的信息是:",student)
            i += 1
            search_id_index = students.index(student)
            user_want = input("是否想要修改用户的信息(Y/N):")
            if user_want in ['Y','y']:
                student['name'] = input("请输入用户的姓名:")
                student['sex'] = input("请输入用户的性别:")
                age_modify = int(input("请输入用户的年龄:"))
                age(age_modify)
                student['age'] = age
                student['tel'] = input("请输入电话号码:")
                student['address'] = input("请输入家庭地址:")
                print("修改后的用户信息是:",student)
                break
            elif user_want in ['N','n']:
                print("不修改用户信息,退出修改!")
                break
            else:
                print("请输入正确的请求!(Y/y/N/n)")
                break
    if i == 0:
        print("搜索的用户ID不存在哦!")
    print("当前的用户数据信息如下:",students)

# add函数
def user_add():
    # 找到目前最后一个元素的ID，添加的数据的ID是这一个ID加1
    id = students[-1]['id'] + 1
    print("当前ID是:",id)
    name = input("请输入用户的姓名:")
    sex = input("请输入用户的性别:")
    age_add = int(input("请输入用户的年龄:"))
    age(age_add)
    tel = input("请输入电话号码:")
    add = input("请输入家庭地址:")
    students.append({'id':id,'name':name,'sex':sex,'age':age_add,'tel':tel,'add':add})
    print("添加后的用户列表如下:",students)

# del函数
def user_del():
    del_id = int(input("请输入修改学生编号:"))
    #i的作用是用来区分是输入的del_id是否在学生统计信息里
    i = 0
    for student in students:
        if student['id'] == del_id:
            print(student)
            i += 1
            del_id_index = students.index(student)
            user_want = input("是否想要修改用户的信息(Y/N):")
            if user_want in ['Y','y']:
                del students[del_id_index]
                break
            elif user_want in ['N','n']:
                print("不想删除用户信息,退出!")
                break
            else:
                print("请输入正确的请求!(Y/y/N/n)")
                break
    if i == 0:
         print("想要删除的学生编号不存在,请输入正确的学生编号")
    print(students)
# 根据用户的操作进行调用相应的函数，如果输入的操作不是定义的操作类型就提醒用户，并退出程序
if action == 'query':
    user_query()
elif action == 'modify':
    user_modify()
elif action == 'add':
    user_add()
elif action == 'del':
    user_del()
else:
    print("请输入正确的操作(query/modify/add/del)")
    exit()


'''
批注: 7.5

优点:
1. 学习函数，使用函数组织代码
2. 编写不完全的增删改查版本
3. 对用户操作进行回显
4. 考虑到list中用户数据ID递增，使用最后一位学生id+1 作为新学生ID
5. 修改用户直接使用用户的引用


改进点:
1. 代码中尽量不要使用exit功能直接结束程序
2. 考虑用循环让用户输入操作指令进行循环操作

'''