# 命名空间
'''
locals
globals
builtins
'''
# 作用域的查找顺序
'''
LEGB: locals enclosing（相邻的上一级） globals builtins 
'''


# 闭包
def func():
    n = 10

    def func2():
        print("func2", n)

    return func2     # 闭包


r = func()
print(r)
r()
