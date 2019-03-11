import socket

# HOST这里写web服务器所在机器的ip，端口地址
HOST, PORT = '', 8888

# 创建socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 调用bind绑定到指定的IP和端口
listen_socket.bind((HOST, PORT))
# 调用listen监听端口
listen_socket.listen()
print('Serving HTTP on port %s ...' % PORT)
while True:
    # 调用accept接受客户端的请求
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    # 将收到请求信息从bytes转换为string
    print(request.decode("utf-8"))
    # web服务器响应（头部+内容）
    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    # 将发送请求信息从string转换为bytes
    client_connection.sendall(http_response.encode("utf-8"))
    # 关闭服务器发送链接
    client_connection.close()