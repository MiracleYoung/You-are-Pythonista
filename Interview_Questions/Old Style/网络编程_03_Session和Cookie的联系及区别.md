# 网络编程_03_Session和Cookie的联系及区别


## Question
说明 Session 和 Cookie 的联系及区别

----

## Answer
一、Session 和 Cookie 的联系
Session 对 Cookie 的依赖：Cookie 采用客户端存储，Session 采用的服务端存储的机制。Session 是针对每个用户（浏览器端）的，Session 值保存在服务器上，通过 SessionId 来区分哪个用户的 Session。因此 SessionId 需要被绑定在浏览器端。SessionId 通常会默认通过 Cookie 在浏览器端绑定，当浏览器端禁用 cookie 时，可通过 Url 重写（可以在地址栏看到 sessionid=KWJHUG6JJM65HS2K6 之类的字符串）或者表单隐藏字段的方式将 SessionId 传回给服务器，以便服务通过 SessionId 获取客户端对应的 Session。

具体一次的请求流程：当程序需要为客户端创建一个 Session 的时候，服务器首先检测这个客户端请求里面是否已经包含了 Session 的表示（SessionId）,如果已经包含，则说明已经为客户端创建过一个 Session，服务端根据 SessionId 检索出来 Sesion 并使用。如果客户端请求不包含 SessionId，则为客户端创建一个 Session，并生成一个 SessionId 返回给客户端保存。

二、Session 和 Cookie 的区别
1. Cookie 数据存放在客户的浏览器上，session 数据放在服务器上。
2. Cookie 不是很安全，别人可以分析存放在本地的 cookie 并进行 cookie 欺骗，考虑到安全应当使用 Session。
3. Session 会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能，考虑到减轻服务器性能方面，应当使用 Cookie。
4. 单个 Cookie 保存的数据不能超过 4K，很多浏览器都限制一个站点最多保存 20 个 Cookie。
5. 可以考虑将登陆信息等重要信息存放为 Session，其他信息如果需要保留，可以放在 Cookie 中。