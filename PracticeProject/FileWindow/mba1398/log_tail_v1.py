"""
* 日志滑动窗口 ---- V1
* 注意查漏补缺
* for else 循环用于处理循环末尾
* namedtuple 命名元组
* mapping  + lambda  高阶映射
* dict(zip(key, value)) 利用 zip() 形成的拉锁关系建立 键值对

"""
from collections import namedtuple
import datetime


names = ['remote_addr', '', '', 'time_local', 'request', 'status', 'body_bytes_sent', '', 'http_user_agent']
LOG = namedtuple('LOG', ['remote_addr', 'time_local', 'method', 'url', 'http',
                         'status', 'body_bytes_sent', 'http_user_agent'])

mapping = {
    'remote_addr': lambda x: x,
    # 时间格式转换 https://www.cnblogs.com/gaosai/p/9825200.html
    'time_local': lambda x:
    datetime.datetime.strptime(x[1:-1], '%d/%b/%Y:%H:%M:%S %z').strftime('%Y-%m-%d %H:%M:%S %z'),
    'method': lambda x: x.strip('"').split()[0],
    'url': lambda x: x.strip('"').split()[1],
    'http': lambda x: x.strip('"').split()[2],
    # 字符转换为 数字 int
    'status': lambda x: int(x),
    'body_bytes_sent': lambda x: int(x),
    # 删除末尾字符
    'http_user_agent': lambda x: x.strip('"\n')
}

tmp = []
ret = []


def extract(line):
    """
    定义抽取函数
    """
    split_flag = True
    for c in line:
        # 特殊符号处理：'[', ']', '"'
        if c == '[':
            split_flag = False
        if c == ']':
            split_flag = True
        if c == '"':
            split_flag = bool(1-split_flag)  # bool 取反
        if c == ' ' and split_flag:
            # 满足分隔符' ' 并且分割标志为 True，就是说：我马上就要分割了，马上进入分割状态
            # 首先要合并分割之前追加的字符
            ret.append(''.join(tmp))
            # 合并完成后呢，清空存放抓取到的字符的临时列表，准备下一次分割
            tmp.clear()
        else:
            # 非分割状态下，临时列表不停的抓取字符
            tmp.append(c)
    else:
        # 缺少这一段，则抽取到的字符缺少最后一个分隔符之后的字符串，这里的作用就是追加上最后一个分隔符之后的字符串
        ret.append(''.join(tmp))

    map_dict = dict(zip(names, ret))
    # 首选使用 zip 函数将字符串的名称和内容建立一对一对应的关系，好像就是拉锁，左边是名称，右边的内容
    # 关系建立好之后，放入字典，名称是 key, 内容是 value
    log = LOG(
        # dict 只是对 nginx 日志默认字段和 nginx 日志内容建立键值对关系，我们需要的信息不止于此，
        # 比如：request 包含 请求的method、url、http type
        # 要获取一个日志字段中的部分内容，这里用到了 mapping + lambda 的高阶方法
        remote_addr=mapping['remote_addr'](map_dict['remote_addr']),
        time_local=mapping['time_local'](map_dict['time_local']),
        method=mapping['method'](map_dict['request']),
        url=mapping['url'](map_dict['request']),
        http=mapping['http'](map_dict['request']),
        status=mapping['status'](map_dict['status']),
        body_bytes_sent=mapping['body_bytes_sent'](map_dict['body_bytes_sent']),
        http_user_agent=mapping['http_user_agent'](map_dict['http_user_agent']),
    )

    return log


LOGFILE = "D:\\pycharm\\pythonista\\log_tail\\access.log"

# 使用 with 函数，随时打开，及时关闭，释放内存
with open(LOGFILE, 'r', encoding='utf-8') as f:
    line =f.readline()
print(line)

log = extract(line)
print(log)
