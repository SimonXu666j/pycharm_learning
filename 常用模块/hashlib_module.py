#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/22 19:24'
import hashlib
m=hashlib.md5()
m.update(b'simon')
print(m.hexdigest())
'''
md5算法特性
    压缩性
    容易计算
    抗修改性
    强抗碰撞
md5用途
    防止被篡改
    防止直接看到明文
    防止抵赖（数字签名）
'''