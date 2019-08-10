# 网络编程_18_url的形式


## Question
url 的形式？

----

## Answer
形式： scheme://host[:port#]/path/…/[?query-string][#anchor]

- scheme：协议(例如：http， https， ftp)
- host：服务器的 IP 地址或者域名
- port：服务器的端口（如果是走协议默认端口，80 or 443）
- path：访问资源的路径
- query-string：参数，发送给 http 服务器的数据
- anchor：锚（跳转到网页的指定锚点位置）
http://localhost:4000/file/part01/1.2.html