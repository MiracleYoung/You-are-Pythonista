# 爬虫_06_让Scrapy框架发送一个post请求

## Question
下列代码，是让Scrapy进行了一个什么操作（）？

```python
class mySpider(scrapy.Spider):
    # start_urls = ["http://www.taobao.com/"]
    def start_requests(self):
        url = 'http://http://www.taobao.com//login'
        yield scrapy.FormRequest(
                        url = url,
                        formdata = {"email": "xxx", "password": "xxxxx"},
                        callback = self.parse_page
                                )
    def parse_page(self, response):
    # do something
```

%!A. requests请求!%

%!B. request请求!%

%!C. post请求!%

%!D. get请求!%

----

## Answer
@!C!@

----

## Analysis

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