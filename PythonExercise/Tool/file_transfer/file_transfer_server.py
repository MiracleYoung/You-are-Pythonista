import socket
import threading
import os
from os.path import getsize


class ftp_server():
    def __init__(self,ip_port):
        self.server = socket.socket()
        self.server.bind(ip_port)
        self.server.listen()

    def tcplink(self,conn, addr):
        print('Accept new connection from {} ...'.format(addr))
        while True:
            data = conn.recv(1024)
            cmd = data.decode()
            print('recv', cmd)
            if cmd == 'dir':
                cmd_result = os.popen(cmd).read()
                conn.send(cmd_result.encode('utf-8'))
            elif cmd.startswith('put'):
                print(cmd)
                conn.send('ack'.encode('utf-8'))
                filesize = conn.recv(1024).decode()
                if filesize:
                    conn.send('ack'.encode('utf-8'))
                    remote_filename = conn.recv(1024).decode()
                    conn.send('ack'.encode('utf-8'))
                    if remote_filename:
                        recvsize = 0
                        with open('{}'.format(remote_filename), 'wb') as write_f:
                            while recvsize < int(filesize):
                                res = conn.recv(1024)
                                write_f.write(res)
                                recvsize += len(res)
                        if recvsize == int(filesize):
                            conn.send('put done !!! plz find file to {}'.format(remote_filename).encode('utf-8'))
                        else:
                            conn.send('lost some data during trasfer...'.encode('utf-8'))
            elif cmd.startswith('get'):
               filename = cmd.split()[1]
               print('filename is {}'.format(filename))
               filesize = getsize(filename)
               conn.send(str(filesize).encode('utf-8'))
               if conn.recv(1024).decode() == 'ack':
                   with open(filename,'rb') as read_f:
                       for line in read_f:
                           conn.send(line)

            else:
                conn.send('Wrong command,plz input agian...'.encode('utf-8'))
    def run(self):
        while True:
            try:
                conn, addr = self.server.accept()
                t = threading.Thread(target=self.tcplink, args=(conn, addr))
                t.start()
            except KeyboardInterrupt:
                self.server.close()



if __name__ == '__main__':
    ip_port = ('localhost',8888)
    f_s = ftp_server(ip_port)
    f_s.run()

