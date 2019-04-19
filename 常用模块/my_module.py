#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/19 9:34'
import sys,os


def sayhi(name):
    print("hello", name)


def saybye(name):
    print("bye", name)


'''
跨模块导入
'''
# sayhi("simon")
# 模块查找路径
# print(sys.path)
print(dir())
print(__file__)  # 程序当前路径
# 获取绝对路径
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)

