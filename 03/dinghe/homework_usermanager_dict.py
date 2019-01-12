# conding:utf-8

# 备注：
    # 1. 由于函数不熟悉，所以没有把用户输入合并
    # 2. 用户查询想实现模糊查询，没有思路
    # 3. 新增用户没有实现排重
    # 4. 查询结果没有格式化
    # 5. 年龄的判断还在优化


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


while True:
    # 打印帮助信息
    help_info()
    # 接收用户输入
    action = input('请输入你的操作：')
    # 进入查询逻辑
    if action == 'query':
        # 接收用户id
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
        # 查询匹配次数变量,用来判断是否有结果返回
        select_cnt = 0

        # 遍历列表，判断查询是否有查询结果
        for student in students:
            # 想实现模糊搜索，但没有思路
            if (input_name == student['name'] and input_sex == student['sex'] and input_age == student['age'] and input_phone == student['telphone'] and input_address == student['address']):
                select_cnt += 1
                # 如果匹配到，就打印信息
                for key, value in student.items():
                    print('%s : %s' % (key, value))
                break
        # 没查询到用户的处理
        if select_cnt == 0:
            print('您查找的用户不存在!!!\n')

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

        # 定义临时列表，用来取最大ID
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
        select_cnt = 0

        # 遍历列表中的字典，并删除
        for student in students:
            if (input_name == student['name'] and input_sex == student['sex'] and input_age == student['age'] and input_phone == student['telphone'] and input_address == student['address']):
                user_info = {'user_id': student['user_id'], 'name': input_name, 'sex': input_sex, 'age': input_age, 'telphone': input_phone, 'address': input_address}
                # 如果匹配到就删除
                students.remove(user_info)
                print('删除成功！')
                continue
        # 为查询到结果处理
        if select_cnt == 0:
            print('您查找的用户不存在!!!\n')

    elif action == 'update':
        # 进入修改逻辑，先查询，后修改
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

        select_cnt = 0

        # 遍历列表，判断查询是否有查询结果
        for student in students:
            # 想实现模糊搜索，但没有思路
            if (input_name == student['name'] and input_sex == student['sex'] and input_age == student['age'] and input_phone == student['telphone'] and input_address == student['address']):
                # 用来定义索引
                user_info = {'user_id': student['user_id'], 'name': input_name, 'sex': input_sex, 'age': input_age, 'telphone': input_phone, 'address': input_address}
                # 配置统计次数，判断是否有匹配结果
                select_cnt += 1
                # 打印匹配到的信息
                for key, value in student.items():
                    print('%s : %s' % (key, value))
                # 接收用户是否修改
                motify_operation = input('请问是否需要修改？（Y/N）')

                # 进入修改逻辑
                if motify_operation == 'y' or motify_operation == 'Y':
                    # 接收用户输入
                    motify_name = input('请输入新的用户名: ')
                    motify_sex = input('请输入新的性别: ')
                    motify_age = input('请输入新的年龄: ')
                    # 判断用户输入年龄是否符合标准
                    if motify_age.isdigit():
                        if int(motify_age) > 0 and int(motify_age) < 80:
                            motify_age = int(motify_age)
                        else:
                            print('请输入新的的年龄')
                            break
                    else:
                        print('请输入正确的年龄')
                        break
                    motify_phone = input('请输入新的电话: ')
                    motify_address = input('请输入新的地址: ')

                    # 设置修改后的用户信息
                    motify_user_info = {'user_id': student['user_id'], 'name': motify_name, 'sex': motify_sex, 'age': motify_age, 'telphone': motify_phone, 'address': motify_address}
                    # 获取索引位置
                    motify_user_index = students.index(user_info)
                    # 修改信息
                    students[motify_user_index] = motify_user_info
                    print('信息修改成功')
                    continue
        if select_cnt == 0:
            print('您查找的用户不存在!!!\n')

    elif action == 'list':
        # 遍历所有人的信息，格式化没做
        for user_info in students:
            print(user_info)
    # 退出机制
    elif action == 'quit' or action == 'exit':
        break
    # 其他情况处理
    else:
        print('您输入的有误，请重新输入')
        continue



'''
批注:8

优点:
1. 预习函数定义和使用
2. 实现增删改查功能融合
3. 考虑对查询结果为空的提示
4. 查询考虑对用户的多项信息进行模糊查询（考虑字符串in和find作用）
5. 考虑对操作结果（成功/失败）的显示


改进点:
1. query逻辑
    考虑82和85行逻辑（可以考虑正常流程应该为输入年龄检查出错后，提醒用户，进行下次操作，而非结束程序）
    查询条件可以输入多个也可以只输入一项针对多项信息进行查询，并且应该是查询条件输入完成后，进行检查，然后进行查询
    考虑查询条件之间的关系，如果有某项输入为空的处理方式
    考虑66行功能，对于查询是否使用（查询可能会有多个查询结果）
    考虑45行，46行对age的转换进行多次的必要性
2. insert逻辑
    考虑94行需要再循环内执行多次的必要性
    考虑如果students默认为空，94行代码什么现象
3. delete逻辑
    操作删除的逻辑都是先按照查询逻辑进行查询（可能会有多行）然后再按照用户唯一编号进行删除
    考虑128行代码必要性
4. update逻辑
    操作更改逻辑都是先按照查询逻辑进行查询，然后再按照用户唯一编号执行修改哪个用户信息
5. 考虑209行必要性

'''