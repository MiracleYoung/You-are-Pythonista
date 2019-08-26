from queue import Queue
from datetime import datetime
from collections import namedtuple
import re
import threading
import time

filename = 'access.log'
data_queue = Queue()
pattern = re.compile(r"\D*(?P<ip>(?:[0-9]{1,3}\.){3}[0-9]{1,3}).*?\[(?P<local_time>.*?)\].*?\"(?P<uri>.*?)\".*?(?P<status>\d+).*?(?P<request_bytes_size>\d+).*?\"(?P<http_refer>.*?)\".*?\"(?P<user_agent>.*?)\"")
Log = namedtuple('Log',['ip', 'local_time', 'request_method', 'request_path', 'request_version', 'status', 'request_bytes_size', 'http_refer', 'user_agent'])

def source(filename):
    with open(filename,'r',encoding='utf-8') as fp:
        lines = fp.readlines()

    for line in lines:
        yield line

def extract(text):
    result = re.match(pattern,text).groupdict()

    ip = result['ip']
    local_time = datetime.strptime(result['local_time'],'%d/%b/%Y:%H:%M:%S %z')

    uri = result['uri'].split()
    request_method = uri[0]
    request_path = uri[1]
    request_version = uri[2]
    status = result['status']
    request_bytes_size = result['request_bytes_size']
    http_refer = result['http_refer']
    user_agent = result['user_agent']
    log = Log(ip,local_time,request_method,request_path,request_version,status,request_bytes_size,http_refer,user_agent)
    return log

def window(data_queue, handle, interval, width):
    now = datetime.now()

    while True:
        current = datetime.now()
        if (current - now).seconds < interval:
            time.sleep(interval)
            continue

        for _ in range(width):
            if data_queue.empty():
                print('work finished, quit...')
                return
            text = data_queue.get()
            result = handle(text)
            print(result)

        now = current

def despatcher(data):
    threadings = list()

    def register(handler, interval, width):
        threadings.append(
            threading.Thread(
                target=window,
                args=(data_queue, handler, interval, width)
            ))

    def start():
        print('load data')
        for item in data:
            data_queue.put(item)

        print('show data')
        for t in threadings:
            t.start()

    return register, start

def main():
    data = source(filename)
    register, start = despatcher(data)
    register(extract, 2, 3)
    start()

if __name__ == '__main__':
    main()

