import os
import sys
import random

print(__file__)#打印当前脚本所在的路径，包含文件名
os.getcwd()#查看当前目录
os.path.isfile(__file__)#判断是否是文件
os.path.isdir(__file__)#判断是否是文件
os.path.abspath(__file__)#获取绝对路径
#os.system("pwd")#执行shell命令


#sys.platform()#返回操作系统名称
#sys.exit('abc')# 退出程序

print(random.choice('abcnasdfqwergasfhetgh'))#随机选取一个字符
print(random.sample('ghdfafgawera sddfh', 3))#随机选取几个字符
a = list(range(20))
random.shuffle(a)#洗牌
print(a)
