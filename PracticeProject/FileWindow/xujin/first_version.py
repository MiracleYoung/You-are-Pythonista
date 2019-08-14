from collections import namedtuple
from datetime import datetime

temp_names = ['remote_address','remote_name','-','time_local','uri','status','request_bytes_size','http_refer','user_agent']
names = ['remote_address','time_local','request_method','request_resource','http_version','status','request_bytes_size','http_refer','user_agent']

def create_log_class():
    Log = namedtuple('Log',names)
    return Log

def read_file():
    with open('access.log','r',encoding='utf-8') as fp:
        text = fp.readline()

        print(text)
    return text

def extract(text):

    result = []
    temp = []
    split = True
    for value in text:
        if value == '[':
            split = False
        elif value == ']':
            split = True
        elif value == '"':
            split = not split

        if value == ' ' and split:
            result.append(''.join(temp))
            temp.clear()
        else:
            temp.append(value)

    result.append(''.join(temp).strip('\n'))
    result_dict = dict(zip(temp_names,result))

    uri = result_dict['uri'].strip('"').split()
    time_local_str = result_dict['time_local'].strip('[').strip(']').split()[0]
    time_local = datetime.strptime(time_local_str,'%d/%b/%Y:%H:%M:%S')

    log_args_map = {
        'remote_address':result_dict['remote_address'],
        'time_local':time_local,
        'request_method':uri[0],
        'request_resource':uri[1],
        'http_version':uri[2],
        'status':result_dict['status'],
        'request_bytes_size':result_dict['request_bytes_size'],
        'http_refer':result_dict['http_refer'],
        'user_agent':result_dict['user_agent']
    }

    return log_args_map

if __name__ == '__main__':
    text = read_file()
    log_args_map = extract(text)
    Log = create_log_class()
    log = Log(**log_args_map)
    print(log)
