# Flask_04_请求上下文和应用上下文的区别和作用

## Question
Flask 中请求上下文和应用上下文的区别和作用？

current_app、g 是应用上下文。

request、session 是请求上下文。

手动创建上下文的两种方法：
1. with app.____()
2. app = current_app._get_current_object()

两者区别：
- 请求上下文：保存了客户端和服务器交互的数据。
- 应用上下文：flask 应用程序运行过程中，保存的一些配置信息，比如程序名、数据库连接、应用信息等。

两者作用：
- 请求上下文(request context)：
Flask 从客户端收到请求时，要让视图函数能访问一些对象，这样才能处理请求。请求对象是一个很好的例子，它封装了客户端发送的 HTTP 请求。

要想让____能够访问请求对象，一个显而易见的方式是将其作为参数传入视图函数，不过这会导致程序中的每个视图函数都增加一个参数，除了访问请求对象,如果视图函数在处理请求时还要访问其他对象，情况会变得更糟。为了避免大量可有可无的参数把视图函数弄得一团糟，Flask使用上下文____把某些对象变为全局可访问。

- 应用上下文(application context)：
它的字面意思是 应用上下文，但它不是一直存在的，它只是 request context 中的一个对 app的代理(人)，所谓 local proxy。它的作用主要是帮助 request 获取当前的应用，它是伴 request 而生，随 ____ 而灭的。

%!A. context, 临时, response!%

%!B. app_context, 永久, response!%

%!C. context, 永久, request!%

%!D. app_context, 临时, request!%

----

## Answer
@!D!@

----

## Analysis

current_app、g 是应用上下文。

request、session 是请求上下文。

手动创建上下文的两种方法：
1. with app.app_context()
2. app = current_app._get_current_object()

两者区别：
- 请求上下文：保存了客户端和服务器交互的数据。
- 应用上下文：flask 应用程序运行过程中，保存的一些配置信息，比如程序名、数据库连接、应用信息等。

两者作用：
- 请求上下文(request context)：
Flask 从客户端收到请求时，要让视图函数能访问一些对象，这样才能处理请求。请求对象是一个很好的例子，它封装了客户端发送的 HTTP 请求。

要想让视图函数能够访问请求对象，一个显而易见的方式是将其作为参数传入视图函数，不过这会导致程序中的每个视图函数都增加一个参数，除了访问请求对象,如果视图函数在处理请求时还要访问其他对象，情况会变得更糟。为了避免大量可有可无的参数把视图函数弄得一团糟，Flask使用上下文临时把某些对象变为全局可访问。

- 应用上下文(application context)：
它的字面意思是 应用上下文，但它不是一直存在的，它只是 request context 中的一个对 app的代理(人)，所谓 local proxy。它的作用主要是帮助 request 获取当前的应用，它是伴 request 而生，随 request 而灭的。