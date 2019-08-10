# Flask_05_Flask项目中如何实现session信息的写入

## Question
Flask 项目中如何实现 session 信息的写入？

Flask 中有三个 session：
- 第一个：数据库中的 session，例如:db.session.add()
- 第二个：在 flask_session 扩展中的 session，使用：from flask_session importSession，使用第三方扩展的 session 可以把信息存储在服务器中，客户端浏览器中只存储 ____。
- 第三个：flask 自带的 session，是一个请求上下文， 使用：from flask import session。自带的session 把信息加密后都存储在客户端的浏览器 ____ 中。
- 
%!A. sessionid, cookie!%

%!B. cookie, sessionid,!%

----

## Answer
@!A!@

----

## Analysis

- Flask 中有三个 session：
  - 第一个：数据库中的 session，例如:db.session.add()
  - 第二个：在 flask_session 扩展中的 session，使用：from flask_session importSession，使用第三方扩展的 session 可以把信息存储在服务器中，客户端浏览器中只存储 sessionid。
  - 第三个：flask 自带的 session，是一个请求上下文， 使用：from flask import session。自带的session 把信息加密后都存储在客户端的浏览器 cookie 中。