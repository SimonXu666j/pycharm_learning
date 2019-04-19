#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/18 14:53'
'''
生成器的创建方式：
    1.列表生成式
    2.函数
'''


def range2(n):
    count = 0
    while count < n:
        print("count", count)
        count += 1
        sign=yield count  # return
        if sign=="stop":
            print("--sign", sign)
            break
    return 3333


new_range = range2(10)  # 变成一个生成器
r1 = next(new_range)
# print(r1)
r2 = next(new_range)
# print(r2)
# new_range.__next__()
# print("做点别的事情")
# new_range.send("stop")

# for i in range(10):
#     print(i)
'''
yield vs return
return：返回并终止函数
yield：返回数据，并冻结当前的执行过程
next：唤醒冻结的函数执行过程，继续执行，直到遇到下一个yield
send：唤醒并继续执行，发送一个信息到生成器内部
'''
