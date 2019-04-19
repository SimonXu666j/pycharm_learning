#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/3/28 16:50'
names = ['alex', 'jack', 'rain']
print(' '.join(names))

s = "Hello World"
print(s.center(50, "="))
print(s.ljust(50, '='))
print(s.rjust(50, '*'))

s1 = "\nHello World  "
print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())

print("加密解密密码表".center(50, "*"))
str_in = "abcdef"
str_out = "#&!*$^"
table = str.maketrans(str_in, str_out)
print(table)
print(s.translate(table))

print("分隔".center(50, "="))
print(s.partition('o'))

print("替换".center(50, "*"))
print(s.replace('o', 'O', 1))

print("分割成列表".center(50, "*"))
print(s.split())
print(s.split('o'))

print("按行分割成列表".center(50, "*"))
a = 'a\nb\nc'
print(a.splitlines())
