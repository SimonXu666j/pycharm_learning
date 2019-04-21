#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/21 17:11'
# 序列化shelve模块
'''
对pickle进行封装，python特有
'''
import shelve

# f = shelve.open('shelve-test')
# names = ["simon", "alex", "test"]
# info = {'name': 'simon', 'age': 25}
# f['names'] = names  # 持久化列表
# f['info_dic'] = info
#
# f.close()
f = shelve.open('shelve-test')
# print(f)
# print(list(f.keys()),list(f.items()))
# print(f.get("names"))
# print(f.get("info_dic"))
# # del f['names']  # 能删除
# f["scores"]=[1,2,3,4,5]  # 能新增
# f["scores"]=[5,4,3,2,1]  # 重新修改赋值
# f.close()
print(f.get("scores"))
