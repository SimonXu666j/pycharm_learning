#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/1 16:12'
print("读文件".center(50, "*"))
f = open(file="filetest", mode="r", encoding="utf-8")
data = f.read()
print(data)
f.close()
print("以二进制的方式读取文件".center(50, "*"))
f = open(file="filetest", mode="rb")
data = f.read()   # 二进制
print(data.decode('utf-8'))
f.close()
print("智能检测编码的工具chardet".center(50,"*"))
import chardet

f = open(file="filetest", mode="rb")
data = f.read()  # 二进制
f.close()
result = chardet.detect(data)
print(result)

print("****************")
f = open(file="filetest", mode="r", encoding="utf-8")
for line in f:
    print(line)
f.close()

print("写文件".center(50, "*"))
f = open(file="writefile", mode="w", encoding="utf-8")
f.write("写文件")
f.close()


print("写文件".center(50, "*"))
f = open(file="writefile2", mode="wb")
f.write("二进制形式写文件".encode("gbk"))
f.close()