# Django_16_cookies与session能单独用吗？

## Question
对 cookies 与 session 的了解？他们能单独用吗？

Session 采用的是在服务器端保持状态的方案，而 Cookie 采用的是在客户端保持状态的方案。但是禁用 Cookie 就不能得到 Session。因为 Session 是用 Session ID 来确定当前对话所对应的服务器 Session，而 Session ID 是通过 Cookie 来传递的，禁用 Cookie 相当于 SessionID，也就得不到 Session。

%!A. Cookie, 服务器端, Session, 客户端!%

%!B. Session,  服务器端, Cookie, 客户端!%

%!C. Session, 客户端, Cookie, 服务器端!%

%!D. Cookie, 客户端, Session, 服务器端!%

----

## Answer
@!B!@

----

## Analysis

Session 采用的是在服务器端保持状态的方案，而 Cookie 采用的是在客户端保持状态的方案。但是禁用 Cookie 就不能得到 Session。因为 Session 是用 Session ID 来确定当前对话所对应的服务器 Session，而 Session ID 是通过 Cookie 来传递的，禁用 Cookie 相当于 SessionID，也就得不到 Session。