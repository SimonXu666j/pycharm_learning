#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/15 10:12'

# 装饰器
user_status = False  # 用户登录了就把这个改成True
#
#
# def login(func):  # 把要执行的模块从这里传进来
#     _username = "alex"  # 假装这是DB里存的用户信息
#     _password = "abc!23"  # 假装这是DB里存的用户信息
#     global user_status
#
#     if user_status == False:
#         username = input("user:")
#         password = input("pasword:")
#
#         if username == _username and password == _password:
#             print("welcome login....")
#             user_status = True
#         else:
#             print("wrong username or password!")
#     else:
#         print("用户已验证通过")
#
#     if user_status == True:
#         func()  # 看这里看这里，只要验证通过了，就调用相应功能


# 装饰器其实就是需要搞个嵌套函数，通过闭包返回内嵌函数
def login(func):  # 把要执行的模块从这里传进来

    def inner(*args,**kwargs):  # 再定义一层函数
        _username = "alex"  # 假装这是DB里存的用户信息
        _password = "abc!23"  # 假装这是DB里存的用户信息
        global user_status

        if user_status == False:
            username = input("user:")
            password = input("pasword:")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")

        if user_status == True:
            func(*args,**kwargs)  # 看这里看这里，只要验证通过了，就调用相应功能

    return inner  # 用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数


def home():
    print("---首页----")


# 装饰器
@login
def america():
    # login()  # 执行前加上验证
    print("----欧美专区----")


def japan():
    print("----日韩专区----")


@login
def henan(style):
    # login()  # 执行前加上验证
    print("----河南专区----",style)


# login(henan)
# login(america)     # 需要验证就调用login，把需要验证的功能 当做一个参数传给login

# henan = login(henan)
# america = login(america)
# # henan
# # america

# america = login(america) #你在这里相当于把america这个函数替换了
# america()
# america()
henan('sss')