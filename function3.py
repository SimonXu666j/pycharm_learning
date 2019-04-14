# 内置方法
'''
abs()     --绝对值
dict()    --转字典
help()
min()     --取最小值
max()     --取最大值
setattr()    --
all()     --判断值是否都是True，空列表也是True
bool()    --判断是否为True
any()     --判断值是否有True，空列表也是False
dir()     --打印程序中所有存在的变量
hex()     --转十六进制
slice()   --切片
divmod()  --取整除
sorted()  --排序
ascii()   --解码成Unicode
enumerate（）   --枚举,返回列表索引和值
oct()     --八进制
bin()     --二进制
eval()    --把字符串解析成代码,只能处理单行代码，有返回值
exec()    --把字符串解析成代码,能处理多行，无返回值
ord()     --返回字符在ASCII码表的位置
chr()     --根据在ASCII码表的位置返回字符
sum()     --求和
bytearray()  --使得字符串能修改，整个字符串内存地址不变，里面子字符改变
filter(func,iterable)    --过滤
map(func,iterable)       --修改
reduce(func,iterable)    --python3中在functools工具包中
pow()       --返回多少次幂
tuple()
callable()   --判断是否可以调用
format()
len()
type()
frozenset()    --不可变的集合
list()
range()
vars()        --打印所有变量名和变量值
locals()    --打印函数的局部变量
globals()   --打印全局变量
repr()
zip()     --压缩两个列表成一个,一一对应，对应不上的丢弃
compile()
reversed()    --反转
complex()    --复数
round()     --保留几位小数
hash()     --把一个字符串变成一个数字
memoryview()
set()
'''
# li=[1,2,3]
# print(enumerate(li))
s = "徐铭"
print(ascii(s))
f = "1+3/2"
print(eval(f))
eval('print("hello world!")')
s = "abcd"
s = s.encode('utf-8')
# s[0]=97
s = bytearray(s)
s[0] = 65
print(s)
import functools
print(functools.reduce(lambda x, y: x + y, [1, 2, 3, 4],10))
print(pow(2,4))

a=[1,2,3,4,5]
b=['a','b','c']
print(list(zip(a,b)))

print(round(1.23423,2))
print(hash('abc'))