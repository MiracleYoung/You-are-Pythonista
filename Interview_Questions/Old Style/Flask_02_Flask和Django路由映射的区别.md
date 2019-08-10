# Flask_02_Flask和Django路由映射的区别？


## Question
Flask 和 Django 路由映射的区别？

----

## Answer
在django中，路由是浏览器访问服务器时，先访问的项目中的url，再由项目中的url找到应用中url，这些url是放在一个列表里，遵从从前往后匹配的规则。

在flask中，路由是通过装饰器给每个视图函数提供的，而且根据请求方式的不同可以一个url用于不同的作用。