import psutil
import time
import socket


def get_ip_address():
    '''
    获取ip地址
    '''
    try:
        # 建立socket连接
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 连接指定ip，端口
        s.connect(('114.114.114.114', 80))
        # 获取ip
        ip = s.getsockname()[0]
        return ip
    finally:
        # 关闭socket连接
        s.close()

def log_generate():
    '''
    生成日志格式
    '''
    # 获取cpu百分比
    cpu_percent = psutil.cpu_percent()
    # 查看系统内存
    mem = psutil.virtual_memory()
    # 计算内存占用百分比
    mem_percent = int(mem.used / mem.total * 100)
    # 获取系统分区信息
    disk_partition = psutil.disk_partitions()
    # 计算系统磁盘占用百分比
    disk_percent = {mount_point : '{} %'.format(psutil.disk_usage('{}'.format(mount_point))[3]) \
                    for mount_point in ( dp.mountpoint for dp in disk_partition )}

    return {get_ip_address():{'cpu': '{} %'.format(cpu_percent), \
                              'mem': '{} %'.format(mem_percent), \
                              'disk':disk_percent, \
                              'time':int(time.time())}}

def main(filepath,counttime=1*60*60,interval=5):
    '''
    循环收集系统信息

    filepath           : 文件路径,
    counttime=1*60*60  : 一小时倒计时
    interval=5         : 间隔默认五秒
    '''
    while counttime > 0:
        # 采集系统信息
        ret = str(log_generate())
        print(ret)
        # 将系统信息数据写入指定文件
        with open(filepath,'a') as f:
            f.write(ret + '\n')
        # 采集参数间隔时间
        time.sleep(interval)
        # 倒计时
        counttime -= interval

if __name__ == '__main__':
    # 指定日志文件路径
    filepath = 'D:\\log.txt'
    # 主函数入口
    main(filepath)
