#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/3/29 17:13'
print("字符编码".center(50, "*"))
'''
UTF-8： 使用1、2、3、4个字节表示所有字符；优先使用1个字符、无法满足则使增加一个字节，最多4个字节。英文占1个字节、欧洲语系占2个、东亚占3个，其它及特殊字符占4个
UTF-16： 使用2、4个字节表示所有字符；优先使用2个字节，否则使用4个字节表示。
UTF-32： 使用4个字节表示所有字符；
'''
print("https://www.cnblogs.com/alex3714/articles/7550940.html")
print("UTF 是为unicode编码 设计 的一种 在存储 和传输时节省空间的编码方案。")
print("编码的转换".center(50, "*"))

"""
UTF-8 --> decode 解码 --> Unicode
Unicode --> encode 编码 --> GBK / UTF-8 ..
"""
"""
常见编码错误的原因有：
    Python解释器的默认编码
    Python源文件文件编码
    Terminal使用的编码
    操作系统的语言设置
"""