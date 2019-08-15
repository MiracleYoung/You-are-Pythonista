import datetime
import queue
import random
import re
import threading
import time
from collections import namedtuple
from pathlib import Path


# 队列
Q = queue.Queue()

# 文件位置
LOG_PATH = Path(__file__).resolve().parent.parent / 'access.log'

# 命名元组 Logs
Logs = namedtuple(
    "Logs", [
        "ip", "times", "method", "routing",
        "http_v", "status", "res_len", "ua"
    ]
)

# 映射
mapping = {
    "times": lambda x: time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.strptime(x, "%d/%b/%Y:%H:%M:%S %z")
        ),
    "status": int,
    "res_len": int,
    "now": lambda: datetime.datetime.now()
}

# 正则预编译, 优化查询效率
regex = re.compile(
    r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(?P<times>.*)\]\s" \
    r"\"(?P<method>.*?)\s(?P<routing>.*?)\s(?P<http_v>.*?)\"\s" \
    r"(?P<status>\d{3})\s(?P<res_len>\d+).*\"(?P<ua>[^\-].*?)\""
)

# 提取数据
with open(LOG_PATH) as f:
    all_logs = f.readlines()


def source():
    """ 加载数据 """
    for log in all_logs:
        yield {"time": mapping["now"](), "line": log}


def extract(line):
    """提取 log 并转换为 Logs

    Args:
        line: 一条日志信息
    
    Returns:
        Logs or None
    """
    infos = re.match(regex, line)
    if infos:
        s_dic = infos.groupdict()
        result = {k: mapping.get(k, lambda x: x)(v) for k, v in s_dic.items()}
        return Logs(
            result['ip'], result['times'], result['method'], result['routing'],
            result['http_v'], result['status'], result['res_len'], result['ua'],
        )
    return None


def window(q: queue.Queue, handler: extract, interval: int, width: int):
    """ 滑动窗口
    
    Args:
        q       : 接收源, 是一个queue, 用于产生数据, 外部数据从 queue 中得到
        handler : 一个函数, 用来处理数据
        interval: 处理的时间间隔
        width   : 窗口宽度
    """
    # 暂存数据
    store = []

    # 开始时间
    start = mapping['now']()

    while True:
        # 获取 log
        try:
            data = q.get_nowait()
        except:
            data = None
        # data = q.get()

        # 获取当前时间
        curent = mapping['now']()
        if data:
            store.append(data)
            # 获取 log 加载时间
            curent = data["time"]
        if (curent - start).total_seconds() >= interval:
            # 更新时间
            start = curent
            # 处理 log
            for log in store:
                log = handler(log["line"])
                if log:
                    print(log.ip, log.times, log.routing, log.ua[:10])

            dt = curent - datetime.timedelta(seconds=width)
            store = [i for i in store if i["time"] > dt]


def despatcher(source: source):
    """  """
    analyers = []

    def register(handler, interval, width):
        analyers.append(threading.Thread(
            target=window,
            args=(Q, handler, interval, width)
        ))
    
    def start():
        for t in analyers:
            t.start()

        for item in source():
            Q.put(item)
    return register, start


if __name__ == "__main__":
    register, start = despatcher(source)
    register(extract, 1, 5)
    start()
