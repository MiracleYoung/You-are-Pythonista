#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/1/28 5:18 AM

__author__ = 'Miracle'


import socket

# server端同样需要通过创建socket，来监听client请求
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 这里和客户端不一样的是，使用的是bind，代表server端自己的ip port
server.bind(('192.168.31.246', 8080))

# 这里的参数5 代表的是同时监听多少个客户端，如果超过5个，那么第6个客户端会出现响应等待，也就是卡在那了
server.listen(5)

print('starting....')
# 创建socket连接后，会返回连接实例和地址
conn, addr = server.accept()

print(conn)
print('client addr', addr)
print('ready to recv the passwd...')

while True:
    # 等待接受客户端发过来的信息
    client_msg = conn.recv(1024)
    print('client passwd changed: %s' % client_msg.decode())

# conn.close()
# server.close()