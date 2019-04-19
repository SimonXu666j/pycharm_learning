# 列表生成式
a = [i + 1 for i in range(10)]
print(a)

# 生成器
a2 = (i for i in range(1000))  # 生成器
print(a2)
# 一个个生成
# print(next(a2))
# print(next(a2))
# print(next(a2))
# print(next(a2))

a3 = (i for i in range(5))
# print(next(a3))
# print(next(a3))
# print(next(a3))
# print(next(a3))
# print(next(a3))
# print(next(a3))   #  生成完了继续生成就报错StopIteration

for i in a3:
    print(i)