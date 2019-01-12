#encoding: utf-8
#初数据格式
students = [
    {
        'id' : 1,
        'name' : 'kk',
        'sex' : '男',
        'age' : 18,
        'tel' : '1888888888',
        'home' : '西安'

    },
    {
        'id' : 2,
        'name' : 'gjw',
        'sex' : '男',
        'age' : 18,
        'tel' : '1888888888',
        'home' : '西安'
    }
]
#菜单选项
nume = {
    'add' : '增加',
    'del' : '删除',
    'update' : '改',
    'search' : '查',
    'q'   : '退出'

}
#主逻辑
while True:
    #初始化添加列表，及id计数器
    new_student = {}
    id_ = 0

    print('欢迎来到学生管理系统,当前学生有: ')
    for i in students:
        print(i)
    for k,v in nume.items():
        print(k,v)
    #选项，通过选项判断执行增删改查退出逻辑
    choose = input('请输入对应功能: ').lower()
    if choose == 'q':
        print('程序退出')
        break
        #增加逻辑，找到列表中id 最大的key赋值给id计数器
    elif choose == 'add':
        for i in students:
            if id_ < i['id']:
                id_ = 0
                id_ += i['id']
        name = input('请输入姓名: ')
        sex = input('请输入性别(男/女):')
        age = int(input('请输入年龄:'))
        #年龄输入如果小于18，大于80程序退出
        if age < 18 or age >80:
            print('年龄错误')
            break
        tel = input('请输入电话号码:')
        home = input('请输入家庭住址：')
        new_student = {
                'id' : id_ +1,
                'name' : name,
                'sex' : sex,
                'tel' : tel,
                'home' : home
        }
        students.append(new_student)
        print('添加成功，当前信息有:',students)
    elif choose == 'del':
        #删除逻辑，索引位0开始，id显示1，通过输入id -1 得出索引位
        del_id = int(input('请输入删除用户id: '))
        del students[del_id -1]
        id_1 = 1
        #所有id 全部重新赋值，依次重新添加值排序
        for i in students:
            i['id'] = 0
            i['id'] += id_1
            id_1 += 1
        print('删除成功，当前信息有:',students)
        #修改逻辑
    elif choose == 'update':
        update_id = int(input('请输入id: '))
        name = input('请输入姓名: ')
        sex = input('请输入性别(男/女):')
        age = int(input('请输入年龄:'))
        if age < 18 or age >80:
            print('年龄错误')
            break
        tel = input('请输入电话号码:')
        home = input('请输入家庭住址：')
        new_student = {
                'id' : update_id,
                'name' : name,
                'sex' : sex,
                'tel' : tel,
                'home' : home
        }
        #通过输入修改的id 索引位-1 得出修改位置，并将用户填写修改信息重新赋值
        students[update_id -1] = new_student
        print(students)
    elif choose == 'search':
        #查询逻辑 for 循环判断 得出id key 是否与输入 id 相等
        search_id = int(input('请输入查询用户id: '))
        for i in students:
            if i['id'] == search_id:
                print(i)
    #如果不是菜单里选项，提示错误，重新开始循环
    else:
        print('输入有误，请重新输入')


'''
批注: 8

优点:
1. 实现增删改查功能融合
2. 考虑对查询结果为空的提示
3. 考虑对操作结果（成功/失败）的显示


改进点:
1. 用户编号作为唯一标识，当用户创建时分配，以后固定不变， 同时注意用户编号和用户所在位置没有关系
2. add逻辑：
    51 和 52行如何简写
    59行作用
3. 用户编号一般作为唯一标识，但是不会根据其进行查询，一般根据可记忆信息或区分性信息进行查询，比如姓名，年龄，地址，电话号码
'''