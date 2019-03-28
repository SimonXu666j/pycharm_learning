#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/3/28 16:15'
print("format".center(50, "="))
info = "hello {0},welcome to {1}!"
info_format = info.format('simon', 'hangzhou')
print(info_format)

print("hello {name},welcome to {city}!".format(name="simon", city="hangzhou"))

person = {"name": "simon", "age": 20}
print("My name is {name} . I am {age} years old .".format(**person))

print("%s".center(50, "*"))
info1 = "hello %s,welcome to %s!" % ('simon', 'hangzhou')
print(info1)
