# 爬虫_12_Scrapy的优缺点


## Question
Scrapy的优缺点?

----

## Answer
优点：
1）scrapy 是异步的
2）采取可读性更强的 xpath 代替正则
3）强大的统计和 log 系统
4）同时在不同的 url 上爬行
5）支持 shell 方式，方便独立调试
5）写 middleware,方便写一些统一的过滤器
6）通过管道的方式存入数据库

缺点：
1）基于 python 的爬虫框架，扩展性比较差
2）基于 twisted 框架，运行中的 exception 是不会干掉 reactor（反应器），并且异步框架出错后是不会停掉其他任务的，数据出错后难以察觉。