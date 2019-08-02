# Django_10_post 和 get的区别?

## Question
post 和 get 的区别?

1.GET是从服务器上____，POST 是向服务器____

2.在客户端，GET 方式在通过 URL 提交数据，数据在 URL 中可以看到，POST 方式，数据放置在 HTML——HEADER 内提交

3.对于 GET 方式，服务器端用____获取变量的值，对于 POST 方式，服务器端用____获取提交的数据
        
%!A. 获取数据, 传送数据, Request.QueryString, Request.Form!%

%!B. 传送数据, 获取数据, Request.Form, Request.QueryString!%

%!C. 获取数据, 传送数据, Request.Form, Request.QueryString!%

%!D. 传送数据, 获取数据, Request.QueryString, Request.Form!%

----

## Answer
@!A!@

----

## Analysis

1.GET 是从服务器上获取数据，POST 是向服务器传送数据

2.在客户端，GET 方式在通过 URL 提交数据，数据在URL中可以看到，POST 方式，数据放置在 HTML——HEADER 内提交

3.对于 GET 方式，服务器端用 Request.QueryString 获取变量的值，对于 POST 方式，服务器端用 Request.Form 获取提交的数据