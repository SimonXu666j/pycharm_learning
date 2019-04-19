#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/3/29 11:20'
info = {}
print("自动生成字典，只有key,value待填写".center(50, "*"))
info_fromkeys = info.fromkeys(['A', 'B', 'C'])
print(info_fromkeys)
print("低效，因为需要字典先转列表".center(50, "*"))
for k, v in info_fromkeys.items():
    print(k, v)
print("推荐使用".center(50, "*"))
for k in info_fromkeys:
    print(k, info_fromkeys[k])
