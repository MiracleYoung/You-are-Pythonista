# -*- coding: utf-8 -*-
from collections import namedtuple
from pathlib import Path
import threading
import datetime
import queue
import time
import re


# 日志路径
log_path = Path(__file__).absolute().parent / 'access.log'
# 日志队列
Q = queue.Queue()

# 日志结构
Logs = namedtuple('Log', 'ip times method routing protocol status_code response_length url ua')
mapping = {
    'times': lambda times: time.mktime(time.strptime(times, '%d/%b/%Y:%H:%M:%S %z')),
}

# 编译正则表达式 提升效率
regex = re.compile(r'(?P<ip>[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}) - - \[(?P<times>.+)\] "(?P<method>.+?) (?P<routing>.+?) (?P<protocol>.+?)" (?P<status>\d+?) (?P<response_length>\d+?) "(?P<url>.*?)" "(?P<ua>.*?)"')


def extract_data(raw_data):
    """ 提取数据

    Arguments:
            raw_data {str} -- 待处理的字符串
    """
    try:
        log_dict = regex.match(raw_data).groupdict()  # 直接将匹配到的内容转化为字典
        log = Logs(
            mapping.get('ip', lambda ip: ip)(log_dict['ip']),
            mapping.get('times', lambda times: times)(log_dict['times']),
            mapping.get('method', lambda mth: mth)(log_dict['method']),
            mapping.get('routing', lambda rou: rou)(log_dict['routing']),
            mapping.get('protocol', lambda pro: pro)(log_dict['protocol']),
            mapping.get('status_code', lambda status: status)(log_dict['status']),
            mapping.get('response_length', lambda len: len)(log_dict['response_length']),
            mapping.get('url', lambda url: url)(log_dict['url']),
            mapping.get('ua', lambda ua: ua)(log_dict['ua'])
        )
        return log
    except Exception:
        print(raw_data)
        print('数据格式有误，匹配出错')
        return None


def source():
    """ 读取文件内容 """
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.readlines()
    for line in content:
        yield line


def window(q, handler, interval, width):
    """窗口滑动 显示数据

    Arguments:
        q {queue.Queue} -- 队列 用于产生数据 存放待显示的内容
        handler {function} -- 处理数据
        interval {integer} -- 滑动时间间隔
        width {[integer]} -- 每次处理的行数
    """
    # 窗口初始化时间
    start_time = datetime.datetime.now()
    log_storage = list()
    while True:
        try:
            data = q.get_nowait()
            # data = q.get()
        except Exception:
            data = None
        if data:
            log_storage.append(data)

        # 当前时间-开始时间 > 时间间隔 应该更新窗口内容
        current_time = datetime.datetime.now()  # 当前时间
        if (current_time - start_time).seconds >= interval:
            print('*' * 50)
            # 更新时间
            start_time = current_time
            # 处理数据
            # 每次处理列表中的前5个数据
            for i in range(width):
                log = handler(log_storage.pop(0))
                # 打印数据 None值检测 正则可能匹配不到数据
                if log:
                    print(f'ip:{log.ip}\nmethod:{log.method}\nrouting:{log.routing}\nstatus_code:{log.status_code}\nres_len:{log.response_length}\nua:{log.ua[:10]}\n')
            print('*' * 50)


def despatcher(source):
    analyers = list()

    def register(handler, interval, width):
        analyers.append(
            threading.Thread(
                target=window,
                args=(Q, handler, interval, width)
            ))

    def start():
        for item in source():
            Q.put(item)

        for t in analyers:
            t.start()

    return register, start


def main():
    register, start = despatcher(source)
    register(extract_data, 1, 3)
    start()


if __name__ == '__main__':
    main()
