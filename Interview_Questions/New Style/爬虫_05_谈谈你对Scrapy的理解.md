# 爬虫_05_谈谈你对Scrapy的理解

## Question
谈谈你对 Scrapy 的理解？

scrapy 是一个为了爬取网站数据，提取结构性数据而编写的应用框架，我们只需要实现少量代码，就能够快速的抓取到数据内容。Scrapy 使用了 ____ 异步网络框架来处理网络通讯，可以加快我们的下载速度，不用自己去实现异步框架，并且包含了各种中间件接口，可以灵活的完成各种需求。

scrapy 框架的工作流程：
1.首先 Spiders（爬虫）将需要发送请求的 url(requests)经 ScrapyEngine（引擎）交给 Scheduler（调度器）。

2.Scheduler（排序，入队）处理后，经 ScrapyEngine，____(可选，主要有 User_Agent， Proxy 代理)交给 Downloader。

3.Downloader 向互联网发送请求，并接收下载响应（response）。将响应（response）经ScrapyEngine，SpiderMiddlewares(可选)交给 Spiders。

4.Spiders 处理 response，提取数据并将数据经 ScrapyEngine 交给 ItemPipeline 保存（可以是本地，可以是数据库）。提取 url 重新经ScrapyEngine 交给 Scheduler 进行下一个循环。直到无Url请求程序停止结束。


%!A. Twisted, DownloaderMiddlewares, SpiderMiddlewares!%

%!B. uvloop, DownloaderMiddlewares, ItemPipeline!%

%!C. Twisted, ItemPipeline, DownloaderMiddlewares!%

%!D. uvloop, ItemPipeline, ItemPipeline!%

----

## Answer
@!A!@

----

## Analysis

scrapy 是一个为了爬取网站数据，提取结构性数据而编写的应用框架，我们只需要实现少量代码，就能够快速的抓取到数据内容。Scrapy 使用了 ____ 异步网络框架来处理网络通讯，可以加快我们的下载速度，不用自己去实现异步框架，并且包含了各种中间件接口，可以灵活的完成各种需求。

scrapy 框架的工作流程：
1.首先 Spiders（爬虫）将需要发送请求的 url(requests)经 ScrapyEngine（引擎）交给 Scheduler（调度器）。

2.Scheduler（排序，入队）处理后，经 ScrapyEngine，____(可选，主要有 User_Agent， Proxy 代理)交给 Downloader。

3.Downloader 向互联网发送请求，并接收下载响应（response）。将响应（response）经ScrapyEngine，SpiderMiddlewares(可选)交给 Spiders。

4.Spiders 处理 response，提取数据并将数据经 ScrapyEngine 交给 ItemPipeline 保存（可以是本地，可以是数据库）。提取 url 重新经ScrapyEngine 交给 Scheduler 进行下一个循环。直到无Url请求程序停止结束。