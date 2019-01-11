#encoding: utf-8
# Author:duanxiaoyong
# Python 3.6
'''
作业要求：用户管理
让用户在控制台上输入”find/list/add/delete/update/exit”格式字符串
如果输入add，则让用户继续输入”用户名:年龄:联系方式”格式字符串，去除前后空字符，并使用:分隔用户数据，将用户数据放入dict中存储，用户名作为key，value使用{name: 用户名, age: 年龄，tel:联系方式}，在放入dict之前检查用户名不重复，如果重复，则提示用户已存在
如果输入delete，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据，若存在数据则将该数据移除，若用户数据不存在，则提示不存在
如果输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，根据用户名查找dcit中数据，若存在数据则将改数据更新数据，若用户数据不存在，则提示不存在
如果用户输入find，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据包含输入字符串的用户信息，并打印
如果用户输入dict，则打印所有用户信息
打印用户第一个行数据为用户信息描述，从第二行开始为用户数据
如果用户输入exit，则打印退出程序，并退出
要求：年龄必须大于10或者小于80 范围值
'''
users = dict()

tpl = '|{:^10}|{:^5}|{:^15}|'
keys = ('name','age','tel')
header = tpl.format(keys[0],keys[1],keys[2])
header_str = '-' * len(header)


#初始化的欢迎信息
print('*********************************************************************')
print('*                     Welcome to User Management                    *')
print('*        You can select a menu number to choose an operation        *')
print('*********************************************************************')

def print_format():
    print(header_str)
    print(header)
    print(header_str)

while True:
    action = input('请输入操作（find/list/add/del/update/exit）:')
    action = action.strip()
    if action =='add':
        users_text = input('请按照规范输入用户信息（用户名：年龄：联系方式：）')
        # users_dict = {'name': '', 'age': '', 'tel': ''}
        users_dict = dict(zip(keys,users_text.split(':')))
        user_name = users_dict.get('name')
        if not users_dict.get('age').strip().isdigit() or users_dict.get('age') < str(18) or users_dict.get('age') >str(80):
            print('添加年龄范围在18-80之间，并且年龄必须是数字，请重新输入')
            continue
        elif user_name in users:
            print('用户已存在，请重新输入')
        else:
            users[user_name] = users_dict
            print('恭喜！添加成功,用户信息如下：')
            print_format()
            for user in users.values():
                print(tpl.format(user['name'], user['age'], user['tel']))

    elif action =='del':
        name = input('请输入查找用户名：')
        print_format()
        for user in users.values():
            print(tpl.format(user['name'], user['age'], user['tel']))
        if users.pop(name.strip(),None):
            print('已删除查找的用户名')
        else:
            print('用户信息不存在')


    elif action =='update':
        users_text = input('请按照规范输入更新的用户信息：')
        users_dict = dict(zip(keys,users_text.split(':')))
        user_name = users_dict.get('name')
        if user_name in users:
            users[user_name] = users_dict
            # users[user_name]['age'] = users_dict.get('age')
            print('用户已更新!')
        else:
            print('用户信息不存在！')

    elif action =='find':
        name = input('请输入查找的用户名：')
        name = name.strip()
        print(header)
        for users_name,user in users.items():
            if users_name.find(name) !=1:
                print(tpl.format(user['name'],user['age'],user['tel']))

    elif action =='list':
        print(header)
        for user in users.values():
            print(tpl.format(user['name'],user['age'],user['tel']))
    elif action =='exit':
        print('退出程序,  欢迎下次登录')
        break


