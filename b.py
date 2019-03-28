#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/3/26 11:16'

count = 0
while count <= 5:
    print("loop", count)
    if count == 5:
        continue
    count += 1

print("-----out of loop-------")
