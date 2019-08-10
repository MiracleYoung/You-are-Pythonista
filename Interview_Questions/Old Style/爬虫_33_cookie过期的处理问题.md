# 爬虫_33_cookie过期的处理问题


## Question
cookie 过期的处理问题？

----

## Answer
因为 cookie 存在过期的现象，一个很好的处理方法就是做一个异常类，如果有异常的话 cookie 抛出异常类在执行程序。