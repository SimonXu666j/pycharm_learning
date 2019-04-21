# random模块
import random, string

print(random.randint(1, 10))  # 包含10
print(random.randrange(1, 10))  # 不包含10
print(random.random())  # 随机浮点
print(random.choice('ahddfie913'))  # 返回字符串中随机字符
print(random.sample('jnauhw27ns', 3))  # 返回多个字符
print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)  # 特殊字符
s = string.ascii_lowercase + string.digits
print(''.join(random.sample(s, 5)))  # 生成5位随机验证码
d = list(range(100))
print(d)
random.shuffle(d)  # 打乱顺序
print(d)
