#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/21 16:55'
# 序列化pickle模块
import pickle
#
# d = {'name': 'simon', "age": 25}
# l = [1, 2, 3, 4, 5, 6]
# pk=open('data.pkl','wb')
# # print(pickle.dumps(d))   # 转成bytes类型
# pickle.dump(d,pk)
f=open('data.pkl','rb')
d=pickle.load(f)
print(d)