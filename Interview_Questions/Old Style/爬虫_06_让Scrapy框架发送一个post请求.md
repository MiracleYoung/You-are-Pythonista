# 爬虫_06_让Scrapy框架发送一个post请求


## Question
怎么样让 scrapy 框架发送一个 post 请求？

----

## Analysis
我们需要借助FormRequest

----

## Answer
```python
class mySpider(scrapy.Spider):
    # start_urls = ["http://www.taobao.com/"]
    def start_requests(self):
        url = 'http://http://www.taobao.com//login'
    # FormRequest 是 Scrapy 发送 POST 请求的方法
        yield scrapy.FormRequest(
                        url = url,
                        formdata = {"email": "xxx", "password": "xxxxx"},
                        callback = self.parse_page
                                )
    def parse_page(self, response):
    # do something
```