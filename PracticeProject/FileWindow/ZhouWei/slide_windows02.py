# coding = utf-8
"""
@author: zhou
@time:2019/8/13 9:48
@File: slide_windows01.py
"""

from collections import namedtuple
from pathlib import Path
import re
import queue
import threading
import time

path = Path()

rege_ip = r'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)'
rege_time = r'[\[][0-3][0-9][/][A-Za-z]{1,3}[/]\d{1,4}[:][0-1]\d[:][0-5][0-9][:][0-5][0-9].*?[\]]'
rege_method = r'[A-Za-z]{1,3}'
rege_uri = r'[/][A-Za-z0-9-/?\[\].=&,]*'
rege_portocol = r'[A-Za-z]*[/][0-9.]*'
rege_code = r'[0-9]*'
rege_size = r'[0-9]*'
rege_ua = r'[A-Za-z0-9/. (;]*'

rege = r'(?P<IP>%s) - - (?P<time>%s) "(?P<method>%s) (?P<uri>%s) (?P<protocol>%s)" (?P<code>%s) (?P<size>%s) "-" "(?P<ua>%s)' \
       % (rege_ip, rege_time, rege_method, rege_uri, rege_portocol, rege_code, rege_size, rege_ua)

pattern = re.compile(rege)
q = queue.Queue()

mystr = """61.151.226.189 - - [10/Aug/2016:08:53:23 +0800] "GET /wp-admin/load-scripts.php?c=1&load[]=jquery-core,jquery-migrate,utils,jquery-ui-core,jquery-ui-widget,jquery-ui-mouse,jquery-ui-sortable,postbox,plupload&ver=4.4.2 HTTP/1.1" 200 93048 "http://www.178linux.com/wp-admin/post.php?post=32459&action=edit&message=10" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
"""

mystr2 = """115.231.8.168 - - [10/Aug/2016:03:21:28 +0800] "GET / HTTP/1.1" 200 46005 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"

"""


def handler(log):
    res = pattern.search(log)
    error_list = []
    if res:
        return res.groupdict()
    else:
        # print("rege failed for: ", mystr1)
        error_list.append(log)
        return error_list


def source():
    with open('access.log') as f:
        log_data = f.readlines()
    for line in log_data:
        yield {"time": time.time(), "line": line}


def windows(q, handler, interval, width):
    s_time = time.time()
    print(q)
    print(q.qsize())
    while True:
        try:
            data = q.get_nowait()
        except:
            data = None
        print(data)
        if data:
            c_time = data['time']
            # print(c_time - s_time)
            if (c_time - s_time) >= interval:
                s_time = c_time
                mydata = handler(data['line'])
                # print("mydata-out: ", mydata)
                if isinstance(mydata, dict):
                    print("mydata: ", mydata)
                else:
                    print("解析日志失败")
                    print(mydata)
        else:
            print("what??")
            break


def despatcher(source):
    analyser = []

    def register(handler, interval, width):
        analyser.append(threading.Thread(
            target=windows,
            args=(q, handler, interval, width)
        ))

    def start():
        for t in analyser:
            print(t)
            t.start()
        for item in source():
            # print("item: ", item)
            q.put(item)

    return register, start


if __name__ == '__main__':
    register, start = despatcher(source)
    register(handler, 2, 10)
    start()
    # a = handler(mystr2)
    # print(a)
    # print(type(a))
    # despatcher = despatcher(q, source, handler, 2, 10)
    # despatcher.register()
    # despatcher.start()
    # a = source()
    # print(a)
    # for i in a:
    #     print(i)

