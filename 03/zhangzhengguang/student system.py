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

#装饰器-实现修改功能    不能修改名字。。。。
def deco(f):
    '''该装饰器为了修改学生信息'''
    def modify():
        result = f()  #调用find()函数
        # print(result)
        if result is not None:  #校验学生信息
            print(result)      #校验不通过返回详细错误值
            return '输入错误'

        if input('do u want to modify the student\'s info(y/n):') == 'y':
            '''实现修改功能，以此类推可实现插入、删除'''
            i = input('what do u want to modify?:')
            index1 = st[name].index(i)
            st[name][index1] = input('input modified info:')

            f2 = open('student_new','wb') # pickle 修改后的信息序列化至新文件中
            pickle.dump(st,f2)

        print(st[name])
    return modify

name = input('请输入查询的学生姓名：')  #无处安放的灵魂。。先放这吧。。

@deco
def find():
    # name = input('请输入查询的学生姓名：')
    if name not in st.keys():
        return '输入name错误'
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

find()  #执行



'''
批注: 2

优点:
1. 自学能力强，学习函数以及装饰器的使用、文件使用、pickle模块使用

建议：
1. 在基础知识的基础上进行扩展学习
'''