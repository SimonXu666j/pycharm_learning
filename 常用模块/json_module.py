#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/21 16:05'
import json
# 序列化json模块
'''
把内存里的数据转变成字符串，以使其能存储到硬盘或通过网络传输到远程，因为硬盘或网络传输时只能接受bytes

'''
'''
把内存数据转成字符，叫序列化  dump dumps
把字符转成内存数据，叫反序列化 load loads
'''

# data = {
#     'roles': [
#         {'role': 'moster', 'type': 'pig', 'life': 50},
#         {'role': 'hero', 'type': 'jianhao', 'life': 80}
#     ]
# }
# d = json.dumps(data)
# print(d, type(d))
# dumps是仅仅把内存数据变成字符串，dump除了转成字符串还有把字符串存到文件的作用
# f = open('test.json', 'w')
# json.dump(data, f)  # 要传文件对象f，python3.x dump可以dump多次，但是load无法load多次(不建议dump多次)，python2.x可以
# d2=json.loads(d)
# print(d2['roles'])

f = open('test.json', 'r')
data = json.load(f)
print(data)
'''
只是把数据类型转成字符串存到内存里的意义？
json.dumps json.loads
1.把内存数据通过网络共享给远程其他人
2.跨平台跨语言去共享数据，定义了不同语言之间的交互规则
'''

'''
json能序列化的数据类型
    str int tuple list dict
pickle
    支持python里的所有数据类型
    只能在python里使用，不跨平台
'''