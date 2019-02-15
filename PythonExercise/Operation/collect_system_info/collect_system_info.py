#!/usr/bin/env python
# coding:utf8
import time
import string

def collector_load():
    ''' 
    系统负载信息收集  
    '''
    # 读取系统负载信息
    load_file = open("/proc/loadavg")
    content = load_file.read().split()
    # 关闭文件
    load_file.close()
    # 生成1分钟，5分钟，15分钟负载对应的字典
    load_avg = {
        "load1": string.atof(content[0]),
        "load5": string.atof(content[1]),
        "load15": string.atof(content[2])
    }
    return load_avg


def collect_memory_info():
    '''
    系统内存信息收集
    '''
    memory_buffer = {}
    # 读取内存信息，并生成字典
    with open("/proc/meminfo") as mem_file:
        for line in mem_file:
            # 过滤出所要信息
            memory_buffer[line.split(':')[0]] = string.atoi(line.split(':')[1].split()[0])
    mem_total = memory_buffer["MemTotal"]
    mem_free = memory_buffer["MemFree"] + memory_buffer["Buffers"] + memory_buffer["Cached"]
    mem_cache = memory_buffer["Cached"]
    mem_info = {
        "mem_total": mem_total,
        "mem_free": mem_free,
        "mem_cache": mem_cache
    }
    return mem_info


def should_handle_device(device):
    '''
    根据磁盘文件名称，判断机器类型
    '''
    normal = len(device) == 3 and device.startswith("sd") or device.startswith("vd")
    aws = len(device) >= 4 and device.startswith("xvd") or device.startswith("sda")
    return normal or aws


def collect_io_info():
    '''
    采集系统磁盘io信息
    '''
    io_buffer = {}
    # 读取系统磁盘io信息
    with open("/proc/diskstats") as io_file:
        for line in io_file:
            line_fields = line.split()
            device_name = line_fields[2]
            # 没数据就继续
            if line_fields[3] == "0":
                continue
            # 是否存在对应磁盘
            if should_handle_device(device_name):
                # /proc/diskstats的解释，可以参见http://www.cnblogs.com/zk47/p/4733143.html
                io_buffer[device_name] = {
                    "ReadRequest": string.atoi(line_fields[3]),
                    "WriteRequest": string.atoi(line_fields[7]),
                    "MsecRead": string.atoi(line_fields[6]),
                    "MsecWrite": string.atoi(line_fields[10]),
                    "MsecTotal": string.atoi(line_fields[12]),
                    "Timestamp": int(time.time())
                }
    return io_buffer



def should_collect_card(line):
    '''
    采集相应网卡
    '''
    return line.startswith("eth") or line.startswith("em")

def collect_net_info():
    '''
    采集网卡流量数据
    '''
    net_buffer = {}
    # 读取磁盘网络信息
    with open("/proc/net/dev") as net_file:
        for line in net_file:
            # 过滤掉非数据行
            if line.find(":") < 0:
                continue
            card_name = line.split(":")[0].strip()
            # 是否存在对应网卡
            if should_collect_card(card_name):
                line_fields = line.split(":")[1].lstrip().split()
                # /proc/net/dev的解释，可以参见https://blog.csdn.net/yzy1103203312/article/details/77848192
                net_buffer[card_name] = {
                    "InBytes": string.atoi(line_fields[0]),
                    "InPackets": string.atoi(line_fields[1]),
                    "InErrors": string.atoi(line_fields[2]),
                    "InDrops": string.atoi(line_fields[3]),
                    "OutBytes": string.atoi(line_fields[8]),
                    "OutPackets": string.atoi(line_fields[9]),
                    "OutErrors": string.atoi(line_fields[10]),
                    "OutDrops": string.atoi(line_fields[11])
                }
    return net_buffer


if __name__ == '__main__':
    print(collector_load())
    print(collect_memory_info())
    print(collect_io_info())
    print(collect_net_info())