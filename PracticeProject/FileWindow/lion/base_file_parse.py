# -*- coding: utf-8 -*-
from collections import namedtuple
import time


tmp = list()
ret = list()

# 构建字典的key values在ret中存放
names_key = ['ip', ' ', ' ', 'times', 'method&routing&http_v', 'status', 'response_length', '-', 'UA']

Logs = namedtuple('Log', ['ip', 'times', 'method', 'routing', 'status', 'http_v', 'response_length', 'UA'])
# 此写法可以替代其他语言中的switch
mapping = {
    'ip': lambda ip: ip,
    'times': lambda datetime: time.mktime(time.strptime(datetime, '%d/%b/%Y:%H:%M:%S %z')),  # 将时间格式化成时间戳
    # 请求方法 请求路径 http协议版本都是存放在一个字符串中 直接通过空格分隔 取值即可
    'method': lambda method: method.split()[0],
    'routing': lambda routing: routing.split()[1],
    'http_v': lambda http_v: http_v.split()[2],
    'status': lambda status: int(status),
    'response_length': lambda length: int(length),
    'UA': lambda user_agent: user_agent.strip('\n')
}


# 处理数据 数据中的每项内容按照空格分隔 遍历字符串 去除脏数据 按照空格组成需要的内容
# [ ] " 是不需要的 遍历到此项时 不需要添加到结果集中 同时说明该符号开始后，每一项内容里的空格是包括在每一项中的
def extract_data(data):
    need_split = True  # 判断是否为闭合符号
    for i in data:
        # '[' ']' '"' 中包裹的内容是单独的一项 因此遇到此元素是需要添加标记
        if i == '[':
            need_split = False
        elif i == ']':
            need_split = True
        elif i == '"':
            need_split = not need_split
        elif i == ' ' and need_split:
            # 说明每项内容到了结尾的地方 需要添加到结果集中
            ret.append(''.join(tmp))
            tmp.clear()  # 清空临时数据
        else:
            tmp.append(i)
        # print(tmp)
    else:  # 结尾处已经没有空格 需要手动添加最后一个空格后的内容
        ret.append(''.join(tmp))
    # 构建字典 将提取出来的内容与key对应
    tmp_dict = dict(zip(names_key, ret))
    log = Logs(
        ip=mapping['ip'](tmp_dict['ip']),
        times=mapping['times'](tmp_dict['times']),
        method=mapping['method'](tmp_dict['method&routing&http_v']),
        routing=mapping['routing'](tmp_dict['method&routing&http_v']),
        http_v=mapping['http_v'](tmp_dict['method&routing&http_v']),
        status=mapping['status'](tmp_dict['status']),
        response_length=mapping['response_length'](tmp_dict['response_length']),
        UA=mapping['UA'](tmp_dict['UA']),
    )

    return log


def main():
    with open('./access.log', 'r', encoding='utf-8') as f:
        first_line = f.readline()

    print(first_line)

    data = extract_data(first_line)
    print(data)


if __name__ == '__main__':
    main()
