#!/usr/bin/python3
#Author:zhangzhengguang
# -*- coding: utf-8 -*-
# @Time   :2019/1/11 18:59

import pickle

dict1 = dict(高嘉伟 = ['男',25,'beijing'],
             区春潮 = ['男',25,'beijing'],
             李宽 = ['男',25,'xi\'an'],
             陈艳涛 = ['男',25,'beijing'],
             郭佳媛 = ['女',23,'beijing'],
            )

f = open('student_list','wb')
pickle.dump(dict1,f)
f.close()

f1 = open('student_list','rb')
st = pickle.loads(f1.read())

'''查'''
# def find():
#     name = input('请输入查询的学生姓名：')
#     if name not in st.keys():
#         print('输入name错误')
#         return find()
#     sex = input('请输入学生的性别：')
#     if sex not in st[name]:
#         print('输入sex错误')
#         return find()
#     age = int(input('请输入学生年龄：'))
#     if age not in st[name]:
#         print('输入age错误')
#         return find()
#     province = input('请输入省份：')
#     if province not in st[name]:
#         print('输入province错误')
#         return find()
#     else:
#         print(name,st[name])
# find()


'''修改'''

#装饰器-实现修改功能
def deco(f):
    '''该装饰器为了修改学生信息'''
    if name not in st.keys():
        return 'name not right!'
    def modify(name):
        f(name)   # 调用查询校验学生信息的find函数
        if input('do u want to modify the student\'s info(y/n):') == 'y':
            i = input('what do u want to modify?:')
            index1 = st[name].index(i)
            st[name][index1] = input('input modified info:')
            
            f2 = open('student_new','wb') # pickle 修改后的信息序列化至新文件中
            pickle.dump(st,f2)

        print(st)
    return modify

name = input('请输入查询的学生姓名：')  #把这个单独拿出来是为了节省代码，实际可直接放到源函数中

@deco
def find(name):
    # name = input('请输入查询的学生姓名：')
    # if name not in st.keys():
    #     return '输入name错误'
    sex = input('请输入学生的性别：')
    if sex not in st[name]:
        return '输入sex错误'
    age = int(input('请输入学生年龄：'))
    if age not in st[name]:
        return '输入age错误'
    province = input('请输入省份：')
    if province not in st[name]:
        return '输入province错误'
    else:
        print(name,st[name])

find(name)  #执行
