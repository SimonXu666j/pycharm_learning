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

# print("写文件".center(50, "*"))
# f = open(file="writefile", mode="w", encoding="utf-8")
# f.write("写文件")
# f.close()
#
#
# print("写文件".center(50, "*"))
# f = open(file="writefile2", mode="wb")
# f.write("二进制形式写文件".encode("gbk"))
# f.close()

# print("追加模式".center(50,"*"))
# f=open(file="writefile",mode = "a",encoding = "utf-8")
# f.write("\n追加模式")
# f.close()

print("混合操作文件".center(50,"*"))
# f = open(file="filetest", mode="r+", encoding="utf-8")
# data = f.read()
# print(data)
# f.write("\nnewline 1哈哈")
# f.write("\nnewline 2哈哈")
# f.write("\nnewline 3哈哈")
# f.write("\nnewline 4哈哈")
# print("new content",f.read())
# f.close()

# f = open(file="filetest", mode="w+", encoding="utf-8")
# data = f.read()
# print(data)
# f.write("\nnewline 1哈哈")
# f.write("\nnewline 2哈哈")
# f.write("\nnewline 3哈哈")
# f.write("\nnewline 4哈哈")
# print("new content", f.read())
# f.close()


"""
读写r+
    先读后写
写读w+(不常用，会把之前的覆盖)
    先写后读
"""
print("其他的文件操作".center(50,"*"))
"""
flush()
readable()
tell()    --按字节算
seek()    --按字节算
read()    --按字符算
readline()
fileno() 
seekable()
truncate()    --按指定长度截断文件
writeable()
"""

# print("文件修改功能".center(50, "*"))
# f = open("modify_file", mode = "r+", encoding = "utf-8")
# f.seek(6)
# f.write("路飞学城")
# f.close()

# print("一边读一边写".center(50,"*"))
# old_str="修改"
# new_str="新修改"
# f=open("modify_file", mode = "r", encoding = "utf-8")
# f_new=open("new_modify_file",mode = "w",encoding = "utf-8")
# for line in f:
#     if old_str in line:
#         line=line.replace(old_str,new_str)
#     f_new.write(line)
# f.close()
# f_new.close()
# 重命名
import os
#os.rename("new_modify_file","modify_file")

print("全部读到內存再写".center(50,"*"))
f_name="rwfile"
old_str="大王"
new_str="小弟"
f=open(file = f_name,mode = "r+",encoding ="utf-8")
data=f.read()
# print(data)
# print(type(data))
data=data.replace(old_str,new_str)
# print(data)
print(f.tell())
f.seek(0)
f.write(data)
f.close()