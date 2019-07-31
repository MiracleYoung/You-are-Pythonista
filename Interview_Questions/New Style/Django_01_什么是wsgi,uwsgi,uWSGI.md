# Django_01_什么是wsgi,uwsgi,uWSGI?

## Question

什么是wsgi,uwsgi,uWSGI?

WSGI: ____服务器网关接口，是一套协议。用于接收用户请求并将请求进行初次封装，然后将请求交给web框架.

uwsgi: 与WSGI一样是一种通信协议，它是uWSGI服务器的独占协议，用于定义传输信息的类型.

uWSGI: 是一个____服务器，实现了WSGI的协议，uWSGI协议，____协议

%!A. web, web, http!%

%!B. http, http, https!%

%!C. web, http, http!%

%!D. http, web, https!%

------

## Answer

@!A!@

------
## Analysis

WSGI: web服务器网关接口，是一套协议。用于接收用户请求并将请求进行初次封装，然后将请求交给web框架。

实现wsgi协议的模块：wsgiref,本质上就是编写一socket服务端，用于接收用户请求（django)

werkzeug,本质上就是编写一个socket服务端，用于接收用户请求(flask)

uwsgi: 与WSGI一样是一种通信协议，它是uWSGI服务器的独占协议，用于定义传输信息的类型。

uWSGI: 是一个web服务器，实现了WSGI的协议，uWSGI协议，http协议
