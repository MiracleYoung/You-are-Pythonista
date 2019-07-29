# 网络编程_16_使用 Socket 套接字需要传入哪些参数


## Question
使用 Socket 套接字需要传入哪些参数 ？

----

## Analysis


----

## Answer
Address Family 和 Type，分别表示套接字应用场景和类型。

family 的值可以是 AF_UNIX(Unix 域，用于同一台机器上的进程间通讯)，也可以是 AF_INET（对于 IPV4 协议的 TCP 和 UDP）。

至于 type 参数，SOCK_STREAM（流套接字）或者SOCK_DGRAM（数据报文套接字）,SOCK_RAW（raw 套接字）。