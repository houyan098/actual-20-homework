# -*- encoding:utf-8 -*-

students = [
    (1, 'kk', '男', 30, '15200000001', '西安市'),
    (2, '薛刚强', '男', 29, '15211110002', '西安市'),
    (3, '高嘉伟', '男', 28, '15200000003', '西安市'),
    (4, '张争光', '男', 27, '15200000004', '西安市'),
    (5, '郭佳媛', '女', 26, '15200000005', '西安市'),
]
property = [('id', 'name','sex', 'age', 'telephone', 'addr'),
]

new_student = []
for i in students:
    for j in property:
        new_student.append(dict((zip(j, i))))
print(new_student)
print(new_student[-1])


'''
输入
    让用户输入姓名
    让用户输入性别
    让用户输入年龄
    让用户输入电话号码
    让用户输入家庭住址

为输入用户设置编号
    找最大的编号

    最大编号 + 1

组成用户元组放置到学生列表中（追加）
'''
def age_Check(age):
        if age.isdigit():
            if int(age) < 80 and int(age) > 10:
                #pass
                #print("参数Age通过检测")
                return True
            else:
                #print("请输入合规的Age： 10 < age < 80")
                return False
        else:
            #print("Age仅为纯数字")
            return False


def user_add():
    id_new = int(new_student[-1]['id']) + 1
    name = input('请输入姓名: ')
    sex = input('请输入性别(男/女):')
    telephone = input('请输入电话号码:')
    addr = input('请输入家庭住址：')
    age = input('请输入年龄：')
    # 定义Age参数最大错误次数 = 3
    for i in range(3):
        if age_Check(age):
            print("GoGoGo")
            break
        elif i == 2:
            print("错误次数超过3次，本程序退出")
        else:
            age = input('请输入年龄：')
    print('当前用户的编号:', id_new)
    student = {'id': id_new, 'name': name, 'sex': sex, 'age': int(age), 'telephone': telephone, 'addr': addr}
    print('当前学生信息:', student)
    new_student.append(student)
    print('所有学生信息:', new_student)

def user_del():
    #定义用户存在状态
    global exist
    exist = 0
    #请输入用户唯一ID信息，用于删除用户数据
    user_Wait_Del = input("请输入需要删除的用户ID信息")
    for i in new_student:
        if i['id'] == int(user_Wait_Del):
            #开始删除操作
            #print(i['name'])
            exist += 1
        else:
            pass
            #异常或退出
    if exist == 0:
        print("用户对象不存在，请输入正确的ID")
        print(exist)
    elif exist > 1:
        print("警告：此ID对应" + str(exist) +"对象")
        print(exist)
    else:
        #假设数据是按照增序排列,并且第一个序号为1
        new_student.pop(int(user_Wait_Del) - 1)
        print(exist)
        pass
    #print(len(new_student))
    #print(new_student)


def user_query():
    #定义用户存在状态
    global exist_query
    exist_query = 0
    #请输入用户唯一ID信息，用于删除用户数据
    user_Wait_Query = input("请输入需要删除的用户ID信息")
    for i in new_student:
        if i['id'] == int(user_Wait_Query):
            #开始删除操作
            #print(i['name'])
            exist_query += 1
            pass
            #异常或退出
    if exist_query == 0:
        print("用户对象不存在，请输入正确的ID")
        #print(exist_query)
    elif exist_query > 1:
        print("警告：此ID对应" + str(exist_query) +"对象")
        for i in range(exist_query):
            print(new_student[int(user_Wait_Query) - 1])
        #print(exist_query)
    else:
        print(new_student[int(user_Wait_Query) - 1])
        #print(exist_query)
        pass
    #print(len(new_student))
    #print(new_student)

def user_modify():
    #定义用户存在状态
    global exist_modify
    exist_modify = 0
    #请输入用户唯一ID信息，用于删除用户数据
    user_Wait_Modify = input("请输入需要修改的用户ID信息")
    for i in new_student:
        if i['id'] == int(user_Wait_Modify):
            #开始删除操作
            #print(i['name'])
            exist_modify += 1
            pass
            #异常或退出
    if exist_modify == 0:
        print("用户对象不存在，请输入正确的ID")
        #print(exist_modify)
    elif exist_modify > 1:
        print("警告：此ID对应" + str(exist_modify) +"对象")
        for i in range(exist_modify):
            print(new_student[int(user_Wait_Modify) - 1])
        #print(exist_modify)
    else:
        #开始获取用户输入，进行修改
        name = input('请输入新的姓名: ')
        sex = input('请输入新的性别(男/女):')
        telephone = input('请输入新的电话号码:')
        addr = input('请输入新的家庭住址：')
        age = input('请输入新的年龄：')
        # 定义Age参数最大错误次数 = 3
        for i in range(3):
            if age_Check(age):
                print("Age参数通过校验")
                break
            elif i == 2:
                print("错误次数超过3次，本程序退出")
                break
            else:
                age = input('请输入新的年龄：')
        new_student_modify={'name': name, 'sex': sex, 'telephone': telephone, 'addr': addr, 'age': age}
        #循环遍历参数是否为Null,忽略空参数
        print(new_student_modify)
        for x in new_student_modify:
            if new_student_modify[x]:
                print("开始修改属性：" + x)
                new_student[int(user_Wait_Modify) - 1][x] = new_student_modify[x]
            else:
                continue
        print(new_student[int(user_Wait_Modify) - 1])
