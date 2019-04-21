# os模块
import os

print(os.getcwd())
print(os.listdir())
# os.remove()    #  删除一个文件
# os.removedirs()  #  删除多个目录
os.path.isdir()
os.path.isfile()
os.path.isabs()  # 判断是否是个绝对路径
os.path.exists()  # 判断路径是否存在
os.path.split()  # 把目录和文件名分开
os.path.splitext()  # 分离扩展名
os.path.dirname()  # 获取路径名
os.path.abspath()  # 获取绝对路径
os.path.basename()  # 获取文件名
os.system()  # 运行shell命令
os.getenv()  # 获取系统环境变量
os.environ  # 返回操作系统所有环境变量
os.environ.setdefault()  # 设置系统环境变量，仅程序运行时有效
os.linesep  # 给出当前平台使用的行终止符
os.name  # 指示正在使用的平台
# os.rename(old,new)    # 重命名
os.makedirs()  # 递归创建目录
os.mkdir()  # 创建单个目录
# os.stat(file)      # 获取文件属性
# os.chmod(file)     # 修改文件权限与时间戳
# os.path.getsize(fielname)  # 获取文件大小
# os.path.join(dir,filename) # 结合目录名与文件名
# os.chdir(dirname)      # 改变工作目录到
os.get_terminal_size()  # 获取当前终端的大小
os.kill()  # 杀死进程
