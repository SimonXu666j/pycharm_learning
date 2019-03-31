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
print(s2,s3,s1)
"""
在python2中不是Unicode 就是str
"""
"""
py3 
    文件默认编码是 utf-8
    字符串  编码是 Unicode
    
    str=unicode
    PY3 除了把字符串的编码改成了unicode, 还把str 和bytes 做了明确区分， str 就是unicode格式的字符， bytes就是单纯二进制啦
    py3的str=py2的Unicode
    在py3里看字符，必须得是unicode编码，其它编码一律按bytes格式展示
py2
    文件默认编码是 ASCII
    字符串  编码  默认是ASCII
    如果文件头声明了gbk,那字符串编码就是gbk
    Unicode 单独类型   
    bytes==str  一回事
    
    在python2中，字符串进行Unicode编码有两种方式，一种是decode，另外一种是定义的时候加上u，如u'路飞'  
"""