#!/usr/bin/env python
# -*-coding:utf-8-*-

import re

# f = open("兼职联系方式.txt",'r',encoding='utf-8')
#
# data = f.read()
#
#
# phones = re.findall("1[0-9]{10}", data)
#
# print(phones)


# phones = []
#
# for line in f:
#     name, city, height, weight, phone = line.split()
#     if phone.startswith('1') and len(phone) == 11:
#         phones.append(phone)
#
# print(phones)
'''
常用正则表达式符号:
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c
[...]   用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]  不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。

'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
'\s'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
 
'(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}
'''

'''
最常用的匹配语法:
re.match 从头开始匹配
re.search 匹配包含,匹配不到返回None,匹配到返回对象，group()方法取拿到的值
re.findall 把所有匹配到的字符放到以列表中的元素返回
re.split 以匹配到的字符当做列表分隔符
re.sub      匹配字符并替换
re.fullmatch   整个字符串匹配成功就返回re object，否组返回None
re.compile
'''
'''
Flags标识符
re.I  忽略大小写
re.M  多行匹配
re.S  匹配换行符
re.X  加注释
'''
# 分组匹配
r = re.search('([a-z]+)([0-9]+)', 'simon123').groups()
print(r)
r1 = re.search('([a-z]+)(\d+)', 'simon123').groups()
print(r1)
print(re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})", "371481199306143242").groupdict())
s = 'simon23button24alex25'
print(re.split('\d+|#|-', 'simon24hangzhou#xm-xxx'))
print(re.split('\d+|#|-', 'simon24hangzhou#xm-xxx',maxsplit=2))
print(re.split('\|', 'simon|25'))  # 特殊符号转义
print(re.split('\d+', s))
print(re.findall('\d+', s))
print(re.sub('[a-z]+', '_', 'ad123id45xf^&', count=2))
print(re.fullmatch('alex', 'alex123'))
pattern = re.compile('alex123')  # 预先编译匹配规则
print(re.fullmatch(pattern, 'alex123'))
print(re.search('a', 'Alex', re.I))  # 忽略大小写
print(re.search('foo.$', 'foo1\nfoo2\n'))
print(re.search('foo.$', 'foo1\nfoo2\n', re.M))  # 多行匹配
print(re.search('.', '\n'))
print(re.search('.', '\n', re.S))  # 匹配换行符
print(re.search('. #test', 'alex'))
print(re.search('. #test', 'alex', re.X))  #
s='1+2*(6/3+(5+7*4)+(7*8)-(10/2))'
print(re.findall('\([^()]+\)',s))