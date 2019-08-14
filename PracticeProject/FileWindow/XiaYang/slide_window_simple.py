from collections import namedtuple
import time


def extract_data(line):
    tmp = []
    ret = []
    flag = False
    for c in line:
        if c == '[':
            flag = True
        elif c == ']':
            flag = False
        elif c == '\"':
            flag = not flag
        elif c == '\n':
            ret.append(''.join(tmp))
        elif c == ' ' and flag is False:
            ret.append(''.join(tmp))
            tmp.clear()
        else:
            tmp.append(c)

    for _ in range(ret.count('-')):
        ret.remove('-')

    return ret


def mapping_nametuple(extract_data):
    Log = namedtuple('log', ['ip', 'time', 'method', 'path', 'http_version', 'status', 'response_length', 'user_agent'])

    Mapping = {
        'ip': lambda x: x,
        'time': lambda x: time.mktime(time.strptime(x.split()[0], "%d/%b/%Y:%H:%M:%S")),
        'method': lambda x: x.split()[0],
        'path': lambda x: x.split()[1],
        'http_version': lambda x: x.split()[2],
        'status': lambda x: x,
        'response_length': lambda x: x,
        'user_agent': lambda x: x
    }

    try:
        ret_log = Log(
            ip=Mapping['ip'](extract_data[0]),
            time=Mapping['time'](extract_data[1]),
            method=Mapping['method'](extract_data[2]),
            path=Mapping['path'](extract_data[2]),
            http_version=Mapping['http_version'](extract_data[2]),
            status=Mapping['status'](extract_data[4]),
            response_length=Mapping['response_length'](extract_data[4]),
            user_agent=Mapping['user_agent'](extract_data[5])
        )
        return ret_log

    except:
        error_info = 'warning: data {} has something error'.format(extract_data)
        print('{}\n{}\n{}'.format(len(error_info)*'*',error_info,len(error_info)*'*'))
        return False




if __name__ == '__main__':
    start_time = time.time()
    count_line = 0
    with open('./access.log','r') as f:
        for line in f.readlines():
            result = mapping_nametuple(extract_data(line))
            if result is not False:
                print(result)
            count_line += 1
    print('time cost: {},total extract lines: {}'.format(time.time()-start_time,count_line))