# 匿名函数 lambda
# 作用：节省代码量、看着高级
func = lambda x, y: x * y if x < y else x / y
print(func(16, 8))

data = list(range(10))
print(data)
print(list(map(lambda x: x * x, data)))

# for index, i in enumerate(data):
#     data[index] = i * i
# print(data)

# 高阶函数:一个函数接收另外一个函数作为参数或者return一个函数


def func(x, y):
    return x + y


def calc(x):
    return x


f = calc(func)
print(f(5, 9))


# 递归
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)
# def recursion(n):
#     print(n)
#     recursion(n+1)
#
#
# recursion(1)
# 递归与栈的关系,递归执行效率不高，递归次数多会导致栈溢出
def calc(n):
    v=n//2
    print(v)
    if v>0:
        calc(v)
        print(v)


calc(10)

# 阶乘
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


r = factorial(5)
print(r)


# 尾递归优化
def cal(n):
    print(n)
    return calc(n+1)  # 尾递归直接return