#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/3/31 13:58'
s = "路飞学城"
print(s)
# print("在python2中使用".center(50,"*"))
s1 = s.decode("utf-8")
print(s1)
print(type(s1))
s2=s1.encode("gbk") #gbk
print(s2)
print(type(s2))
s3=s1.encode("utf-8") #utf-8
print(s3)
"""
在python2中不是Unicode 就是str
"""
"""
py3 
    文件默认编码是 utf-8
    字符串  编码是 Unicode
py2
    文件默认编码是 ASCII
    字符串  编码  默认是ASCII
    如果文件头声明了gbk,那字符串编码就是gbk
    Unicode 单独类型     
"""