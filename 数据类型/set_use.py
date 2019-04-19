#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/3/29 11:35'
set1 = {1, 2, 3, 'A', 'B', 'C'}
set2 = {3, 4, 5, 'a', 'B', 'c'}
print("交集".center(50, "*"))
print(set1 & set2)
print("并集".center(50, "*"))
print(set1 | set2)
print(set1.union(set2))
print("差集".center(50, "*"))
print(set1 - set2)
print(set1.difference(set2))
print("集合关系测试".center(50, "*"))
print(set1.intersection(set2))
print("并集减交集".center(50, "*"))
print((set1 | set2) - (set1 & set2))
print("对称差集".center(50, "*"))
print(set1.symmetric_difference(set2))
print("超集，子集".center(50, "*"))
set4 = {1, 2, 3}
set5 = {1, 2, 3, 4, 5}
print(set4.issubset(set5))
print(set5.issuperset(set4))
print("判断是否不相交".center(50, "*"))
print(set4.isdisjoint(set5))


print("列表去重变集合".center(50, "*"))
li = [1, 2, 1, 3, 3, 4, 4, 5]
set3 = set(li)
print(set3)
print("增加".center(50, "*"))
set3.add(1)
set3.add(6)
print(set3)
print("删除，随机删".center(50, "*"))
set3.pop()
print(set3)
print("删除，删除指定值".center(50, "*"))
set3.remove(6)
print(set3)
print("remove删除不存在的值会报错，discard不会".center(50, "*"))
# set3.remove(6)
set3.discard(6)
print(set3)
print("update扩展集合".center(50, "*"))
set3.update([11, 12])
print(set3)
print("clear清空".center(50, "*"))
set3.clear()
print(set3)
