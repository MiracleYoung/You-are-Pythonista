# 网络编程_13_HTTP和HTTPS区别


## Question
说说 HTTP 和 HTTPS 区别？

----

## Answer
HTTP 协议传输的数据都是未加密的，也就是明文的，因此使用 HTTP 协议传输隐私信息非常不安全，为了保证这些隐私数据能加密传输，于是网景公司设计了 SSL（Secure Sockets Layer）协议用于对 HTTP 协议传输的数据进行加密，从而就诞生了 HTTPS。
简单来说，HTTPS 协议是由 SSL+HTTP 协议构建的可进行加密传输、身份认证的网络协议，要比 http 协议安全。

HTTPS 和 HTTP 的区别主要如下：
1、https 协议需要到 ca 申请证书，一般免费证书较少，因而需要一定费用。
2、http 是超文本传输协议，信息是明文传输，https 则是具有安全性的 ssl 加密传输协议。
3、http 和 https 使用的是完全不同的连接方式，用的端口也不一样，前者是 80，后者是 443。
4、http 的连接很简单，是无状态的；HTTPS 协议是由 SSL+HTTP 协议构建的可进行加密传输、身份认证的网络协议，比 http 协议安全。