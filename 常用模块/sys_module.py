# sys模块
import sys

# sys.argv   # 命令行参数List，第一个元素默认是程序本身
# sys.exit(n)  # 退出程序
print(sys.version)  # 打印python解释器版本
print(sys.maxsize)  # 打印int最大值
print(sys.path)
print(sys.platform)
print(sys.stdout)  # 标准输出
# sys.stdout.write('simon')
# sys.stdin.readline()  # 标准输入
print(sys.getrecursionlimit())  # 获取最大递归层数
# sys.setrecursionlimit(1200)  #设置最大递归层数
print(sys.getdefaultencoding())  # 获取解释器默认编码
print(sys.getfilesystemencoding())  # 获取内存数据存到文件里的默认编码
