#!/usr/bin/python
# coding=utf-8

import urllib2
import sys
import os

# 这里填入你需要检测的web页面
url = 'http://127.0.0.1/index.html'
# 调用urllib2方法
req = urllib2.Request(url)
try:
    # 调用urllib2方法
    fp = urllib2.urlopen(req)
    reault = fp.read()
    # 如果get不到结果就如下处理
    if not reault:
        print "\033[31mtomcat was stopped!\033[0m"
        # 调用linux shell命令
        os.system('service tomcat restart')
        # 退出，返回2状态码
        sys.exit(2)
# 如果捕获到http异常，就如下处理
except urllib2.URLError, urllib2.HTTPError:
    print "\033[31mtomcat was stopped!\033[0m"
    # linux shell命令
    os.system('service tomcat restart')
    # 退出，返回2状态码
    sys.exit(2)

# 如果上面的代码块都没执行到，说明tomcat服务正常运行!"
print "tomcat is work"
# 退出，返回0状态码
sys.exit(0)

