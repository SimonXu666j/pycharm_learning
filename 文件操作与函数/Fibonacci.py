#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/18 10:49'


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# fib(10)


def fib(max):
    n, a, b = 0, 0, 1

    while n < max:
        print("before yield")
        yield b   # 把函数的执行过程冻结在这一步，并且把b的值返回给外面的next()
        print(b)
        a, b = b, a + b

        n += 1

    return 'done'


print(fib(10))
f = fib(10)    # 把函数变成一个生成器
next(f)
# next(f)
# next(f)
# next(f)

# while True:
#     next(f)

# for i in f:
#     print(i)

'''
生成器可以把里面的值返回给外面，函数的话只能直接打印出来
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
'''