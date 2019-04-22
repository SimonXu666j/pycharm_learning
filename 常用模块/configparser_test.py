#!/usr/bin/env python
# -*-coding:utf-8-*-

import configparser

config = configparser.ConfigParser()
config.read("conf_test.ini")      # 打开文件读取
print(dir(config))
print(config.options("group1"))   # 打印group1下面的options
print(config["group2"]["k1"])
config.add_section("group3")      # 添加group3这个section
config["group3"]['name']="simon"  # 给group3这个section添加options
config["group3"]['age']="25"
# config.set('group2','k2',11111)
# config.remove_option('group1','k2')   # 删除group1这个section下面的k2option
config.remove_section("group1")         # 删除group1这个section
config.write(open("conf_test2.ini","w"))   # 写入新文件
# config.write(open("conf_test_new.ini","w"))


