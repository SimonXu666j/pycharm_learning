#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/3/28 15:37'
import copy
print("=======copy数据半共享（复制其数据独立内存存放，但是只拷贝成功第一层）======")
l1 = [1, 2, 3, [11, 22, 33]]
l2 = l1.copy()
print(l2)  # [1,2,3,[11,22,33]]
l2[3][2] = 'aaa'
print(l1)  # [1, 2, 3, [11, 22, 'aaa']]
print(l2)  # [1, 2, 3, [11, 22, 'aaa']]
l1[0] = 0
print(l1)  # [0, 2, 3, [11, 22, 'aaa']]
print(l2)  # [1, 2, 3, [11, 22, 'aaa']]
print(id(l1) == id(l2))  # Flase
print("======直接赋值======")
'''
=赋值：数据完全共享（=赋值是在内存中指向同一个对象，如果是可变(mutable)类型，比如列表，修改其中一个，另一个必定改变
如果是不可变类型(immutable),比如字符串，修改了其中一个，另一个并不会变）
'''
x = [1, 2, 3]
y = x
print(x)
print(y)
x.pop()
print(x)
print(y)
print("=========clear=============")
n = ['a', 'b', 'c']
print(n)
n.clear()
print(n)
print("========deepcopy深拷贝：数据完全不共享==========")
a = [1, 2, 3]
b = copy.deepcopy(a)
print(a)
print(b)
a.append(4)
print(a)
print(b)