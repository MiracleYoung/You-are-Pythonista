import time
import re
from collections import namedtuple


log = namedtuple('logs',['ip','times','method','routing','http_v','status','response_length','UA'])
mapping = {

    'ip':lambda x:x.split(' ')[0],
    'times':lambda x:time.mktime(time.strptime(x.strip('['),'%d/%b/%Y:%H:%M:%S')),
    'method':lambda x:x,
    'routing':lambda x:x,
    'http_v':lambda x:x,
    'status':lambda x:x,
    'response_length':lambda x:int(x),
    'UA':lambda x:x.strip('\n')
}

def extract(lines):
    '''
    此方法用于抽取数据
    :param lines: 日志文件
    :return: 抽取后的数据
    '''
    for line in lines:
        new_line = line.replace('"',' ').replace('-','')
        splits = re.split(' {2,}',new_line)
        try:
            ip = splits[0]
            times = splits[1].split(' ')[0]
            method_routing_http_v = splits[2].split(' ')
            method = method_routing_http_v[0]
            routing = method_routing_http_v[1]
            http_v = method_routing_http_v[2]
            status_res = splits[3].split(' ')
            status = status_res[0]
            responseLense = status_res[1]
            UA = splits[4]
            logs = log(
                ip = mapping['ip'](ip),
                times = mapping['times'](times),
                method = mapping['method'](method),
                routing = mapping['routing'](routing),
                http_v = mapping['http_v'](http_v),
                status = mapping['status'](status),
                response_length = mapping['response_length'](responseLense),
                UA = mapping['UA'](UA)

            )

        except Exception as e:
            continue
        yield logs

if __name__ == '__main__':
    with open('../data/access.log','r') as f:
        lines = f.readlines()
    for i in extract(lines):
        print(i)

