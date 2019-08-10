# 爬虫_21_对于Scrapy_redis的理解


## Question
对于 scrapy_redis 的理解。

----

## Answer
scrapy-redis 是一个基于 redis 的 scrapy 组件，通过它可以快速实现简单分布式爬虫程序，该组件本质上提供了三大功能：
- scheduler - 调度器
- dupefilter - URL 去重规则（被调度器使用）
- pipeline - 数据持久化

scrapy-redis 组件
1. URL 去重 
去重规则通过 redis 的集合完成，去重规则中将 url 转换成唯一标示，然后在 redis 中检查是否已经在集合中存在
2. 调度器 
调度器，调度器使用 PriorityQueue（有序集合）、FifoQueue（列表）、LifoQueue（列表）进行保存请求，并且使用 RFPDupeFilter 对 URL 去重
3. 数据持久化
定义持久化，爬虫 yield Item 对象时执行 RedisPipeline 将 item 持久化到 redis 时，指定 key 和序列化函数 REDIS_ITEMS_KEY = '%(spider)s:items' REDIS_ITEMS_SERIALIZER = 'json.dumps'
使用列表保存 item 数据
4. 起始 URL 相关
获取起始 URL 时，去集合中获取还是去列表中获取？True，集合；False，列表
REDIS_START_URLS_AS_SET = False # 获取起始URL时，如果为True，则使用self.server.spop；
如果为 False，则使用 self.server.lpop。
编写爬虫时，起始 URL 从 redis 的 Key 中获取。