# conding:utf-8


students = [
    {'user_id': 1, 'name': 'kk', 'sex': '男', 'age': 30, 'telphone': '15200000000', 'address': '西安市'},
    {'user_id': 2, 'name': '薛刚强', 'sex': '男', 'age': 30, 'telphone': '15211110000', 'address': '西安市'},
    {'user_id': 3, 'name': '高嘉伟', 'sex': '男', 'age': 30, 'telphone': '15200000000', 'address': '西安市'},
    {'user_id': 4, 'name': '张争光', 'sex': '男', 'age': 30, 'telphone': '15200000000', 'address': '西安市'},
    {'user_id': 5, 'name': '郭佳媛', 'sex': '男', 'age': 30, 'telphone': '15200000000', 'address': '西安市'},
    {'user_id': 6, 'name': '丁贺', 'sex': '男', 'age': 32, 'telphone': '13811732735', 'address': '北京市'}
]


def help_info():
    # 输出提示
    print('欢迎光临用户管理系统!')
    print('查询输入query')
    print('增加请输入insert')
    print('删除请输入delete')
    print('修改请输入update')
    print('查看所有人请输出list')
    print('退出请输入exit/quit')


action = ''
while True:
    help_info()
    # 接收用户输入
    action = input('请输入你的操作：')
    # 进入查询逻辑
    if action == 'query':
        # 接收用户id
        select_cnt = 0
        user_name = input('请输入你的用户名: ')
        for student in students:
            if user_name == student.get('name'):
                select_cnt += 1
                for key, value in student.items():
                    print('%s : %s' % (key, value))
                    break
        if select_cnt == 0:
            print('您查找的用户不存在!')

    elif action == 'insert':
        # 接收用户输入
        input_name = input('请输入你的用户名: ')
        input_sex = input('请输入你的性别: ')
        input_age = input('请输入你的年龄: ')
        # 判断用户输入年龄是否符合标准
        if input_age.isdigit():
            if int(input_age) > 0 and int(input_age) < 80:
                input_age = int(input_age)
            else:
                print('请输入正确的年龄')
                break
        else:
            print('请输入正确的年龄')
            break
        input_phone = input('请输入你的电话: ')
        input_address = input('请输入你的地址: ')

        # 定义临时列表
        tmp_list = []
        # 获取所有用户ID，取最大值+1
        for student in students:
            tmp_list.append(student['user_id'])
            new_id = max(tmp_list) + 1
        new_user_info = {'user_id': new_id, 'name': input_name, 'sex': input_sex, 'age': input_age, 'telphone': input_phone, 'address': input_address}
        # 将用户信息追加到列表中
        students.append(new_user_info)
        # 打印新增信息
        print('用户信息添加完成')
        for key, value in new_user_info.items():
            print('%s : %s' % (key, value))

    elif action == 'delete':
        # 接收用户输入
        input_name = input('请输入你的用户名: ')
        input_sex = input('请输入你的性别: ')
        input_age = input('请输入你的年龄: ')
        # 判断用户输入年龄是否符合标准
        if input_age.isdigit():
            if int(input_age) > 0 and int(input_age) < 80:
                input_age = int(input_age)
            else:
                print('请输入正确的年龄')
                break
        else:
            print('请输入正确的年龄')
            break
        input_phone = input('请输入你的电话: ')
        input_address = input('请输入你的地址: ')

        # 遍历列表中的字典，并删除
        for student in students:
            if (input_name == student['name'] and input_sex == student['age'] and input_age == student['age'] and input_phone == student['telphone'] and input_address == student['address']):
                user_info = {'user_id': student['user_id'], 'name': input_name, 'sex': input_sex, 'age': input_age, 'telphone': input_phone, 'address': input_address}
                print(user_info)
                del students[user_info]
                print('删除成功！')
                print(students)
                continue

    elif action == 'update':
        pass
    elif action == 'list':
        for user_info in students:
            print(user_info)
    elif action == 'quit' or action == 'exit':
        break
    else:
        print('您输入的有误，请重新输入')
        continue
