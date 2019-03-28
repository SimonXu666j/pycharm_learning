#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/3/26 11:22'


class TestOne:
    pass


count = 0
while count < 5:
    count += 1
    print('loop', count)

else:
    print("循环正常执行完成")

print("-----out of loop----")


# count = 0
# while count < 5:
#     print('loop', count)
#     if count == 3:
#         break
#     count += 1
# else:
#     print("循环正常执行完成")
#
# print("-----out of loop----")
