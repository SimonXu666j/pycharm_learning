#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/22 17:18'
import configparser
'''
ConfigParser 是用来读取配置文件的包。配置文件的格式如下：中括号“[ ]”内包含的为section。
section 下面为类似于key-value 的配置内容。
括号“[ ]”内包含的为section。紧接着section 为类似于key-value 的options 的配置内容。
'''

config = configparser.ConfigParser()
config.read("conf.ini")
print(config.sections())
print(config.default_section)
# print(list(config["bitbucket.org"].keys()))
print(config["bitbucket.org"]["User"])
if 'user' in config["bitbucket.org"]:
    print('in ')

