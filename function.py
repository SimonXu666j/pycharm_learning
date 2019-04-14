def sayhi(city, *args, name = "simon"):
    for msg in args:
        print("hello " + name + " " + city + " " + msg)


# 位置参数，顺序赋值
# 默认参数必须放在最后
# 关键参数必须放在位置参数之后
# 非固定参数 *args  **kwargs
# sayhi("hangzhou")
# sayhi("shanghai", "ming")
sayhi("hangzhou", "a", "b", "c")


def func(name, *args, **kwargs):
    print(name, args, kwargs)


func("simon", 24, "tesla", "500w", addr = "hangzhou", num = 123456)

name = "simon"
print(name)


# 在函数内修改全局变量使用global
def change_name():
    global name
    name = "simonxu"
    print(name)

change_name()
print(name)

# 在函数里修改列表数据
names = ["simon", "button", "xuming"]


def change_names():
    # names=["simon","button"]
    del names[2]
    names[0] = "xuming"
    print(names)


change_names()
print(names)

# 嵌套函数
# age=19
# def func1():
#     def func2():
#         print(age)
#
#     age = 23
#     func2()
#
# func1()

age = 19


def func1():
    global age

    def func2():
        print(age)

    # age = 23
    func2()
    age = 23


func1()
print(age)


# 作用域 Python中函数就是一个作用域
# 代码定义完成后，作用域已经生成，作用域链向上查找
age = 18


def func1():
    age = 23

    def func2():
        print(age)

    return func2


val = func1()
val()
