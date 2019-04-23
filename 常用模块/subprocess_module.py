#!/usr/bin/env python
# -*-coding:utf-8-*-
import subprocess
print(dir(subprocess))
# subprocess.run()
# a = subprocess.run(['df', '-h'])
# print(a.returncode, a.args)
# a.check_returncode()
# a=subprocess.run(['df','-h'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
# print(a.stdout)
# print(a.stderr)
a = subprocess.run('df -h|grep disk1', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# subprocess.call()
# a = subprocess.call(['df','-hT'],shell=True)    # shell=True意思交给系统去执行shell命令
subprocess.call(['df', '-h'])

# Popen()方法
'''
subprocess.Popen()：
在一些复杂场景中，我们需要将一个进程的执行输出作为另一个进程的输入。
在另一些场景中，我们需要先进入到某个输入环境，然后再执行一系列的指令等。
这个时候我们就需要使用到suprocess的Popen()方法。该方法有以下参数：
    args：shell命令，可以是字符串，或者序列类型，如list,tuple。
    bufsize：缓冲区大小，可不用关心
    stdin,stdout,stderr：分别表示程序的标准输入，标准输出及标准错误
    shell：与上面方法中用法相同
    cwd：用于设置子进程的当前目录
    env：用于指定子进程的环境变量。如果env=None，则默认从父进程继承环境变量
    universal_newlines：不同系统的的换行符不同，当该参数设定为true时，则表示使用\n作为换行符
'''
# a = subprocess.Popen('mkdir subprocesstest',shell=True,cwd='/root')
# Popen对象创建后，主程序不会自动等待子进程完成。我们必须调用对象的wait()方法，父进程才会等待 (也就是阻塞block)
child = subprocess.Popen('ping -c4 blog.linuxeye.com', shell=True)
child.wait()
print('parent process')

# child.poll() # 检查子进程状态
# child.kill() # 终止子进程
# child.send_signal() # 向子进程发送信号
# child.terminate() # 终止子进程
# child.send_signal()  # 发信号
# child.communicate()  # 与启动的进程交互
