import socket
import threading
import os
from os.path import getsize


class ftp_server():
    '''
    初始化服务器端
    '''
    def __init__(self,ip_port):
        self.server = socket.socket()
        # 绑定ip端口
        self.server.bind(ip_port)
        # 监听
        self.server.listen()

    def tcplink(self,conn, addr):
        '''
        客户端方法实现 
        '''
        print('Accept new connection from {} ...'.format(addr))
        while True:
            # 接收客户端发送命令行
            data = conn.recv(1024)
            cmd = data.decode()
            print('recv', cmd)
            # dir:列出当前目录
            if cmd == 'dir':
                # 在命令行执行dir命令并读取返回结果
                cmd_result = os.popen(cmd).read()
                # 发送命令行返回结果
                conn.send(cmd_result.encode('utf-8'))
            # put:从客户端发送文件到服务器端
            elif cmd.startswith('put'):
                print(cmd)
                # 发送确认信息
                conn.send('ack'.encode('utf-8'))
                # 获取客户端传输文件大小
                filesize = conn.recv(1024).decode()
                if filesize:
                    # 发送确认信息
                    conn.send('ack'.encode('utf-8'))
                    # 接收服务器端需要保存的文件名及路径
                    remote_filename = conn.recv(1024).decode()
                    # 发送确认信息
                    conn.send('ack'.encode('utf-8'))
                    if remote_filename:
                        recvsize = 0
                        # 二进制打开本地文件并写入
                        with open('{}'.format(remote_filename), 'wb') as write_f:
                            # 接受到的文件与客户端发送文件大小一致，退出循环
                            while recvsize < int(filesize):
                                res = conn.recv(1024)
                                write_f.write(res)
                                recvsize += len(res)
                        # 服务端信息发送至客户端
                        if recvsize == int(filesize):
                            conn.send('put done !!! plz find file to {}'.format(remote_filename).encode('utf-8'))
                        else:
                            conn.send('lost some data during trasfer...'.encode('utf-8'))
            # get:从服务端拉取文件到客户端
            elif cmd.startswith('get'):
               filename = cmd.split()[1]
               print('filename is {}'.format(filename))
               # 获取服务端文件大小
               filesize = getsize(filename)
               # 将服务端文件大小发送给客户端
               conn.send(str(filesize).encode('utf-8'))
               # 收到确认信息
               if conn.recv(1024).decode() == 'ack':
                   # 二进制方式读取文件
                   with open(filename,'rb') as read_f:
                       # 遍历二进制文件并发送
                       for line in read_f:
                           conn.send(line)

            else:
                conn.send('Wrong command,plz input agian...'.encode('utf-8'))
    def run(self):
        '''
        服务端实现多线程并发
        '''
        while True:
            try:
                # 接受客户端请求
                conn, addr = self.server.accept()
                # 调用多线程方法,传入服务端方法及参数
                t = threading.Thread(target=self.tcplink, args=(conn, addr))
                t.start()
            except KeyboardInterrupt:
                self.server.close()



if __name__ == '__main__':
    # 这里填入服务器端的ip端口
    ip_port = ('localhost',8888)
    f_s = ftp_server(ip_port)
    f_s.run()

