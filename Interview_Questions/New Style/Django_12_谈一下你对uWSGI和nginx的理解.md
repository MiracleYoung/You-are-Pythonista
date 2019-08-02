# Django_12_谈一下你对uWSGI和nginx的理解？

## Question
谈一下你对 uWSGI 和 nginx 的理解？

1.uWSGI 是一个Web服务器，它实现了 WSGI 协议、uwsgi、http 等协议。Nginx 中 HttpUwsgiModule 的作用是与 uWSGI 服务器进行交换。WSGI 是一种 Web 服务器网关接口。它是一个 Web 服务器（如 nginx，uWSGI 等服务器）与 web 应用（如用 Flask 框架写的程序）通信的一种规范。

要注意 WSGI/uwsgi/uWSGI 这三个概念的区分。

WSGI 是一种____。

uwsgi 是一种____而不是通信协议，在此常用于在 uWSGI 服务器与其他网络服务器的数据通信。

uWSGI 是实现了 uwsgi 和 WSGI 两种协议的Web服务器。

nginx 是一个开源的高性能的 HTTP 服务器和反向代理：

1.作为 web 服务器，它处理____和索引文件效果非常高

2.它的设计非常注重效率，最大支持____万个并发连接，但只占用很少的内存空间

3.稳定性高，配置简洁。

4.强大的反向代理和负载均衡功能，平衡集群中各个服务器的负载压力应用
        
%!A. 线路协议, 通信协议, 动态文件, 10!%

%!B. 通信协议, 线路协议, 静态文件, 10!%

%!C. 通信协议, 线路协议, 静态文件, 5!%

%!D. 线路协议, 通信协议, 动态文件, 5!%

----

## Answer
@!C!@

----

## Analysis

1.uWSGI 是一个 Web 服务器，它实现了 WSGI 协议、uwsgi、http 等协议。Nginx 中HttpUwsgiModule 的作用是与 uWSGI 服务器进行交换。WSGI 是一种 Web 服务器网关接口。它是一个 Web 服务器（如 nginx，uWSG I等服务器）与 web 应用（如用 Flask 框架写的程序）通信的一种规范。

要注意 WSGI/uwsgi/uWSGI 这三个概念的区分。

WSGI 是一种通信协议。

uwsgi 是一种线路协议而不是通信协议，在此常用于在 uWSGI 服务器与其他网络服务器的数据通信。

uWSGI 是实现了 uwsgi 和 WSGI 两种协议的 Web 服务器。

nginx 是一个开源的高性能的 HTTP 服务器和反向代理：

1.作为 web 服务器，它处理静态文件和索引文件效果非常高

2.它的设计非常注重效率，最大支持5万个并发连接，但只占用很少的内存空间

3.稳定性高，配置简洁。

4.强大的反向代理和负载均衡功能，平衡集群中各个服务器的负载压力应用

