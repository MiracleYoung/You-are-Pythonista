import socket
from os.path import getsize
import sys

class ftp_client():
    def __init__(self,ip_port):
        '''
        初始化客户端
        '''
        self.ip_port = ip_port
        self.client = socket.socket()
        # 客户端连接服务端socket
        self.client.connect(self.ip_port)
    def run(self):
        '''
        客户端方法实现 
        '''
        while True:
            try:
                msg = input('ftp_client:>>')
                # 命令行输入为空跳过循环
                if not msg:
                    continue
                # dir:列出当前目录
                elif msg == 'dir':
                    # 将命令传给服务端
                    self.client.send(msg.encode('utf-8'))
                    # 接收服务端dir返回结果
                    data = self.client.recv(1024)
                    print('{}'.format(data.decode()))
                # get:从服务端拉取文件
                elif msg.split()[0] == 'get':
                    # 将命令传给服务端
                    self.client.send(msg.encode('utf-8'))
                    # 接收服务端文件大小
                    file_size = self.client.recv(1024).decode()
                    print('remote file size : {}'.format(file_size))
                    # 获取本地保存文件路径
                    filename = input('Plz input you prepare to save filename and path: ')
                    # 确认接收
                    self.client.send('ack'.encode('utf-8'))
                    recv_size = 0
                    # 二进制打开本地文件并写入
                    with open('{}'.format(filename),'wb') as write_f:
                        # 接受到的文件与服务器端文件大小一致，退出循环
                        while recv_size < int(file_size):
                            res = self.client.recv(1024)
                            write_f.write(res)
                            recv_size += len(res)
                    print(type(recv_size),type(file_size),recv_size == int(file_size))
                    # 客户端显示信息
                    if recv_size == int(file_size):
                        print('get done !!! plz find file to {}'.format(filename))
                    else:
                        print('lost some data during trasfer...')
                # put:从客户端发送文件到服务器端
                elif msg.split()[0] == 'put':
                    # 将命令传给服务端
                    self.client.send(msg.encode('utf-8'))
                    # 获取本地文件名
                    filename = msg.split()[1]
                    # 获取本地文件大小
                    filesize = getsize(filename)
                    print(filesize)
                    # 确认接收
                    if self.client.recv(1024).decode() == 'ack':
                        # 发送本地文件大小至服务器端
                        self.client.send(str(filesize).encode('utf-8'))
                    # 确认接收
                    if self.client.recv(1024).decode() == 'ack':
                        # 获取服务器端将要保存的文件命名及对应路径
                        remoete_filename = input('Plz input filename and path you prepare to put on the remote server: ')
                        # 将文件命名及对应路径发送给服务端
                        self.client.send(remoete_filename.encode('utf-8'))
                    # 确认接收
                    if self.client.recv(1024).decode() == 'ack':
                        # 二进制读取本地文件并读取
                        with open('{}'.format(filename),'rb') as read_f:
                            # 循环遍历发送本地文件
                            for line in read_f:
                                self.client.send(line)
                    # 接收服务端显示信息
                    print(self.client.recv(1024).decode())
                # quit,exit: 退出客户端
                elif msg == 'quit' or msg == 'exit':
                    sys.exit(0)

                else:
                    print('Wrong command,plz input agian...')
            except KeyboardInterrupt:
                self.client.close()



if __name__ == '__main__':
    # 这里填入服务器端的ip端口
    ip_port = ('localhost',8888)
    f_c = ftp_client(ip_port)
    f_c.run()
