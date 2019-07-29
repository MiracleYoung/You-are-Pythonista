# 爬虫_10_Scrapy中的信号


## Question
爬虫向数据库存数据开始和结束都会发一条消息，是 scrapy 哪个模块实现的？

----

## Answer
Scrapy 使用信号来通知事情发生，因此答案是 signals 模块。