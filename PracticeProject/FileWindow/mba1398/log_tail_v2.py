#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 21:28

__author__ = 'mba1398'
"""
滑窗日志进阶版，实现滑窗展示日志，加入报警机制，status > 200 则播放报警声
数据加载--数据分析--数据展示
替换 IP 地址的绝对正则
"""



from collections import namedtuple # 命名元组
from pathlib import Path
import datetime
import time
import threading  # 多线程
import queue # 队列
import re
import winsound


# 日志路径
log_path = Path(__file__).absolute().parent / 'access.log'
# 开启日志队列
queue = queue.Queue()

# 日志结构
LOGS = namedtuple('LOG', ['remote', 'datetime', 'method', 'url', 'protocol',
                         'status', 'size', 'references', 'useragent'])

# 映射
ops = {
    'datetime': lambda timestr: str(datetime.datetime.strptime(timestr, "%d/%b/%Y:%H:%M:%S %z")),
    'request': lambda request: dict(zip(('method', 'url', 'protocol'), request.split())),
    # int 不能使用 ljust, rjust, center 补齐，改为原始的 str，去掉 mapping
    # 'status': int,
    # 'size': int
    }

# 定义正则表达式，预编译，提升效率
# pattern1 = r'''(?P<remote>(\d{1,3}\.){3}\d{1,3}) - - \[(?P<datetime>[^\[\]]+)\] \"(?P<request>[^\"]+)\" (?P<status>\d+) (?P<size>\d+) \"(?P<references>[^\"]+)\" \"(?P<useragent>[^\"]+)\".*'''
pattern2 = r'''(?P<remote>([1-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]).((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){2}(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])) - - \[(?P<datetime>[^\[\]]+)\] \"(?P<request>[^\"]+)\" (?P<status>\d+) (?P<size>\d+) \"(?P<references>[^\"]+)\" \"(?P<useragent>[^\"]+)\".*'''

regex = re.compile(pattern2)


def extract(line):
    try:
        s_dict = regex.match(line).groupdict()
        result = {k: ops.get(k, lambda x: x)(v) for k, v in s_dict.items()}
        return result

    except Exception:
        print(line)
        print('error，匹配出错')
        return None

def source():
    """ 读取文件内容 """
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.readlines()
    for line in content:
        yield line


def window(q, handler, interval, width):
    """
    滑动窗口，显示数据
    :param q: 接收队列数据（本来是source，接收单条，引入队列后，持续接受
    :param handler: 处理数据
    :param interval: 多久处理一次
    :param width: 每次处理多少行日志
    """
    # 窗口初始化时间
    start_time = datetime.datetime.now()
    datas = []
    while True:
        try:
            data = q.get_nowait()
            # data = q.get()
        except Exception:
            data = None
        if data:
            datas.append(data)

        # 当前时间-开始时间 > 时间间隔 应该更新窗口内容
        current_time = datetime.datetime.now()  # 当前时间
        if (current_time - start_time).seconds >= interval:
            print('*' * 10+' Start monitor the log. '+'*' * 10+'\n')
            # 更新时间
            start_time = current_time
            # 处理数据
            # 每次处理列表中的前 width 个数据
            for i in range(width):
                log = handler(datas.pop(0))
                print('remote:{0}|| datetime:{1}\nmethod:{2}|| url:{3} || protocol:{4}\nstatus:{5}|| size:{6}\nreferences: {7}\nuseragent:{8}\n'
                      .format(log['remote'].ljust(15), log['datetime'], log['request']['method'].ljust(15), log['request']['url'].ljust(15), log['request']['protocol'], log['status'].ljust(15), log['size'], log['references'], log['useragent']))
                # 判断访问是否成功，否则报警,并停顿5秒
                if int(log['status']) > 200:
                    winsound.Beep(600, 1000)
                    # 其中600表示声音大小，1000表示发生时长，1000为1秒
                    time.sleep(5)

            print('=' * 10+' OVER! wait for a moment.'+'=' * 10+'\n')


def despatcher(source):
    analyers = []

    def register(handler, interval, width):
        analyers.append(threading.Thread(target=window, args=(queue, handler, interval, width)))

    def start():
        for item in source():
            queue.put(item)

        for t in analyers:
            t.start()

    return register, start


def main():
    register, start = despatcher(source)
    register(extract, 1, 1)
    start()


if __name__ == '__main__':
    main()






