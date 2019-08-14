# coding = utf-8
"""
@author: zhou
@time:2019/8/13 9:48
@File: slide_windows01.py
"""

from collections import namedtuple
from pathlib import Path


path = Path()
split_log = namedtuple("split_log", "ip, time, method, uri, protocol, statuscode, content_size, UA")


mystr = """61.151.226.189 - - [10/Aug/2016:08:53:23 +0800] "GET /wp-admin/load-scripts.php?c=1&load[]=jquery-core,jquery-migrate,utils,jquery-ui-core,jquery-ui-widget,jquery-ui-mouse,jquery-ui-sortable,postbox,plupload&ver=4.4.2 HTTP/1.1" 200 93048 "http://www.178linux.com/wp-admin/post.php?post=32459&action=edit&message=10" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
"""


def log_mapping(logdata):
    """
    :param logdata:
    :return: list
    :备注:
    有部分日志行，存在不规则数据，如字段中存在[]等，导致解析失败
    """
    try:
        ip = logdata[0]
        time = logdata[3]
        method = logdata[4].split(" ")[0]
        uri = logdata[4].split(" ")[1]
        protocol = logdata[4].split(" ")[2]
        statuscode = logdata[5]
        content_size = logdata[6]
        UA = logdata[8]
        return [ip, time, method, uri, protocol, statuscode, content_size, UA]
    except:
        pass


def main_func(logdata):
    data_list = log_mapping(logdata)
    if isinstance(data_list, list):
        result = tuple.__new__(split_log, data_list)
        print("result", result)
    else:
        print(data_list)
        raise
    # print(len(result))
    # for i in map(split_log._make, data_list):  # 不懂这里为啥会报错。。。
    #     print(i)


def split_tools(data):
    switch = True
    tmp = []
    ret = []
    for i in data:
        if i == '[':
            switch = False
        elif i == ']':
            switch = True
        if i == '"':
            switch = not switch
        if i == ' ' and switch:
            ret.append("".join(tmp))
            tmp.clear()
        else:
            if i == '-' or i == '"' or i == '':
                continue
            else:
                tmp.append(i)
    else:
        ret.append("".join(tmp))
    return ret


if __name__ == '__main__':
    """
    测试代码，mystr 里面的字符串，会解析失败
    """
    split_data = split_tools(mystr)
    print(split_data)
    main_func(split_data)
    """
    实际解析时用下面的代码
    """
    # with open('access.log', 'r', encoding='utf-8') as f:
    #     logd_data = f.readlines()
    #     for log in logd_data:
    #         main_func(split_tools(log))
