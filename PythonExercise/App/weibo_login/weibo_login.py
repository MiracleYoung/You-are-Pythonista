#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/12/24 6:19 AM

__author__ = 'Miracle'

import urllib.request
import urllib.parse
from http import cookiejar
import requests
import base64
import re
import json
import hashlib

# 处理cookie，让cookie以后一直跟着走
cj = cookiejar.CookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

postdata = {
    'entry': 'weibo',
    'gateway': '1',
    'from': '',
    'savestate': '7',
    'userticket': '1',
    'ssosimplelogin': '1',
    'vsnf': '1',
    'vsnval': '',
    'su': '',
    'service': 'miniblog',
    'servertime': '',
    'nonce': '',
    'pwencode': 'wsse',
    'sp': '',
    'encoding': 'UTF-8',
    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
    'returntype': 'META'
}


def get_servertime():
    url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=dW5kZWZpbmVk&client=ssologin.js(v1.3.18)&_=1329806375939'
    # 返回出来的是一个Response对象，无法直接获取，text后，可以通过正则匹配到
    # 大概长这样子的：sinaSSOController.preloginCallBack({"retcode":0,"servertime":1545606770, ...})
    data = requests.request('GET', url).text
    p = re.compile('\((.*)\)')
    try:
        json_data = p.search(data).group(1)
        data = json.loads(json_data)
        servertime = str(data['servertime'])
        nonce = data['nonce']
        return servertime, nonce
    except:
        print('获取 severtime 失败!')
        return None


def get_pwd(pwd, servertime, nonce):
    # 第一次计算，注意Python3 的加密需要encode，使用bytes
    pwd1 = hashlib.sha1(pwd.encode()).hexdigest()
    # 使用pwd1的结果在计算第二次
    pwd2 = hashlib.sha1(pwd1.encode()).hexdigest()
    # 使用第二次的结果再加上之前计算好的servertime和nonce值，hash一次
    pwd3_ = pwd2 + servertime + nonce
    pwd3 = hashlib.sha1(pwd3_.encode()).hexdigest()
    return pwd3


def get_user(username):
    # 将@符号转换成url中能够识别的字符
    _username = urllib.request.quote(username)
    # Python3中的base64计算也是要字节
    # base64出来后，最后有一个换行符，所以用了切片去了最后一个字符
    username = base64.encodebytes(_username.encode())[:-1]
    return username


def login():
    username = 'yangqinglin_19900723@hotmail.com'
    pwd = ',yql0723,'
    url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.3.18)'
    try:
        servertime, nonce = get_servertime()
    except:
        return
    global postdata
    postdata['servertime'] = servertime
    postdata['nonce'] = nonce
    postdata['su'] = get_user(username)
    postdata['sp'] = get_pwd(pwd, servertime, nonce)

    postdata = urllib.parse.urlencode(postdata)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    req = requests.request(
        method='POST',
        url=url,
        data=postdata,
        headers=headers
    )
    ret = req.text
    p = re.compile('location\.replace\(\"(.*?)\"\)')
    try:
        login_url = p.search(ret).group(1)
        requests.request('GET', login_url)
        print("登录成功!")
    except:
        print('登陆失败!')

login()