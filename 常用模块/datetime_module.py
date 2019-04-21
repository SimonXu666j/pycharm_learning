# datetime模块
import datetime, time

print(datetime.datetime.now())  # 返回当前的datetime()的日期类型
a = datetime.datetime.now()
print(a.year)
print(datetime.date.fromtimestamp(time.time()))  # 2019-04-20，拿时间戳的年月日
# 时间运算
print(datetime.datetime.now() - datetime.timedelta(1))  # 2019-04-19 15:44:30.856069  datetime.timedelta(1)减去1天
# 时间替换
d = datetime.datetime.now()
print(d.replace(year = 2018, month = 8))  # 替换年月
