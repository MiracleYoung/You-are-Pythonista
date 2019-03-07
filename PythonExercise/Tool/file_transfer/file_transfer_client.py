import socket
from os.path import getsize
import sys

class ftp_client():
    def __init__(self,ip_port):
        self.ip_port = ip_port
        self.client = socket.socket()
        self.client.connect(self.ip_port)
    def run(self):
        while True:
            try:
                msg = input('ftp_client:>>')
                if not msg:
                    continue
                elif msg == 'dir':
                    self.client.send(msg.encode('utf-8'))
                    data = self.client.recv(1024)
                    print('{}'.format(data.decode()))
                elif msg.split()[0] == 'get':
                    self.client.send(msg.encode('utf-8'))
                    file_size = self.client.recv(1024).decode()
                    print('remote file size : {}'.format(file_size))
                    filename = input('Plz input you prepare to save filename and path: ')
                    self.client.send('ack'.encode('utf-8'))
                    recv_size = 0
                    with open('{}'.format(filename),'wb') as write_f:
                        while recv_size < int(file_size):
                            res = self.client.recv(1024)
                            write_f.write(res)
                            recv_size += len(res)
                    print(type(recv_size),type(file_size),recv_size == int(file_size))
                    if recv_size == int(file_size):
                        print('get done !!! plz find file to {}'.format(filename))
                    else:
                        print('lost some data during trasfer...')

                elif msg.split()[0] == 'put':
                    self.client.send(msg.encode('utf-8'))
                    filename = msg.split()[1]
                    filesize = getsize(filename)
                    print(filesize)
                    if self.client.recv(1024).decode() == 'ack':
                        self.client.send(str(filesize).encode('utf-8'))
                    if self.client.recv(1024).decode() == 'ack':
                        remoete_filename = input('Plz input filename and path you prepare to put on the remote server: ')
                        self.client.send(remoete_filename.encode('utf-8'))
                    if self.client.recv(1024).decode() == 'ack':
                        with open('{}'.format(filename),'rb') as read_f:
                            for line in read_f:
                                self.client.send(line)
                    print(self.client.recv(1024).decode())

                elif msg == 'quit' or msg == 'exit':
                    sys.exit(0)

                else:
                    print('Wrong command,plz input agian...')
            except KeyboardInterrupt:
                self.client.close()



if __name__ == '__main__':
    ip_port = ('localhost',8888)
    f_c = ftp_client(ip_port)
    f_c.run()
