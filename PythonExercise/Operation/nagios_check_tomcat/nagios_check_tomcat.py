#!/usr/bin/python
# coding=utf-8

import urllib2
import sys
import os

url = 'http://127.0.0.1/index.html'  # 这里填入你需要检测的web页面
req = urllib2.Request(url)  # 调用urllib2方法
try:
    fp = urllib2.urlopen(req)  # 调用urllib2方法
    reault = fp.read()
    if not reault:  # 如果get不到结果就如下处理
        print "\033[31mtomcat was stopped!\033[0m"
        os.system('service tomcat restart')  # 调用linux shell命令
        sys.exit(2)  # 退出，返回2状态码
except urllib2.URLError, urllib2.HTTPError:  # 如果捕获到http异常，就如下处理
    print "\033[31mtomcat was stopped!\033[0m"
    os.system('service tomcat restart')  # linux shell命令
    sys.exit(2)  # 退出，返回2状态码

print "tomcat is work"  # 如果上面的代码块都没执行到，说明tomcat服务正常运行!"
sys.exit(0)  # 退出，返回0状态码

