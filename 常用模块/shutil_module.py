#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/21 14:31'

# shutil模块
'''
高级的文件、文件夹、压缩包处理模块
'''
import shutil
# 将文件内容拷贝到另一个文件中，可以部分内容
# f1 = open('shutil-test', mode='r')
# f2 = open('shutil-test-new', mode='w')
# shutil.copyfileobj(f1, f2)

# 拷贝文件
shutil.copyfile('shutil-test','shutil-test-copyfile')

# 拷贝权限
shutil.copymode()
# 拷贝状态信息
shutil.copystat()
# 拷贝文件和权限
shutil.copy()
# 拷贝文件和状态信息
shutil.copy2()
# 递归的去拷贝文件
shutil.ignore_patterns()
shutil.copytree()
# 递归去删除文件
shutil.rmtree()
# 递归的去移动文件
shutil.move()
# 创建压缩包并返回文件路径，例如zip、tar
shutil.make_archive(base_name='压缩包名',format='zip')