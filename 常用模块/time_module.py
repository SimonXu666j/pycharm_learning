# time模块
import time

print(time.time())  # 时间戳
print(time.localtime())  # 打印本地时间
a = time.localtime()
print("%s-%s-%s" % (a.tm_year, a.tm_mon, a.tm_mday))
print(time.gmtime())  # 格林尼治时间，把时间戳转换成时间对象
print(time.mktime(a))  # 把时间对象转换成时间戳
time.sleep(2)  # 线程推迟的时间
print(time.asctime())  # Sat Apr 20 15:14:05 2019
print(time.ctime())  # 转时间戳为Sat Apr 20 15:14:05 2019
print(time.strftime("%Y-%m-%d %X"))  # 把时间对象转换成字符串
s = time.strftime("%Y-%m-%d %X")
print(time.strptime(s, "%Y-%m-%d %X"))  # 把字符串转换成时间对象
