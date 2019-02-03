#!/usr/bin/env python
# coding:utf8


import logging
import paramiko
import argparse
import sys
from concurrent import futures
import time
from progressbar import *

# 具体作用参见https://www.jianshu.com/p/9686bfa7e81c
reload(sys)
sys.setdefaultencoding('utf8')


class run(object):
    '''
    定义一个类，类中包含了这个脚本的所有的功能实现函数
    '''
    def __init__(self):
        '''
        生成对象时的初始化操作
        '''
        # 导入update_file.py这个配置文件的getPlatform函数，详见配置文件模板
        from update_file import getPlatform
        # 获取配置文件列表
        self.host_lists = getPlatform()
        # 定义日志打印格式、输出文件文件、日志级别等
        logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='game_update.log',
                filemode='w')


    def argument(self):
        '''
        利用argparse这个模块，自定义脚本的命令行参数
        需要模块用法的请参见：https://blog.ixxoo.me/argparse.html
        '''
        parse = argparse.ArgumentParser()
        # 定义需要执行的线程数参数:-t
        parse.add_argument('--thread-number', '-t', dest='num_value', help='thread number')
        # 定义需要执行的命令行参数:-c
        parse.add_argument('--command-line', '-c', dest='cmd_value', help='command line')
        args = parse.parse_args()
        # 返回args对象
        return args


    def get_hosts(self):
        '''
        从update_file.py这个文件的getPlatform函数内获取服务器列表,详见配置文件模板
        '''
        # 定义一个空的列表
        update_list = []
        # 循环外层列表 ，也就是[['web',(1,100)]，['mysql',(1,10)]]
        for host_name in self.host_lists:
            # 循环内层列表，也就是web-001,web-002,web-003...；mysql-001,mysql-002,mysql-003...）
            for num in range(int(host_name[1][0]), int(host_name[1][1]) + 1):
                # 循环得到的结果，添加至update_list列表
                update_list.append('%s-%03d' % (host_name[0], num))

        # 返回这个列表
        return update_list


    def get_exists_host(self):
        '''
        将从update_file.py配置文件,getPlatform函数里获取的服务器列表与/etc/hosts文件对比，如果有匹配的就输出到新的列表
        '''
        final_list = []
        hosts_lists = []
        # 调用上面那个函数的返回结果
        file_lists = self.get_hosts()
        # 打开操作系统的hosts文件
        with open('/etc/hosts', 'rt') as f:
            # 遍历hosts文件内容
            for line in f.readlines():
                # 这里之所以要增加判断，是为了避免hosts文件里有异常的不合法的结果
                if line and  len(line.split()) >= 2:
                    hosts_lists.append(line.split()[1])
        for x in file_lists:
            # 将配置文件里的服务器列表循环，如果不存在于hosts文件，跳过，不然就加入新的列表（也就是file_lists和hosts_lists两个列表取交集，结果存入list1）
            if x not in hosts_lists:
                continue
            final_list.append(x)
        # 返回最终配置文件与hosts里取的结果
        return final_list


    def remote_ssh(self, ip, cmd):
        '''
        ssh方法定义，参见https://qxf2.com/blog/ssh-using-python-paramiko/
        '''
        # 创建SSH对象
        client = paramiko.SSHClient()
        # 把要连接的机器添加到known_hosts文件中
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(ip)
            # 分别返回标准输入，标准输出，标准错误输出
            stdin, stdout, stderr = client.exec_command(cmd)
            new_std_out = stdout.read()
            new_std_err = stderr.read()
            client.close()
            # 日志里记录执行过的ip和命令行标准、错误输出
            logging.info('{}\n{}'.format(ip,new_std_out))
            logging.error('{}\n{}'.format(ip,new_std_err))
        except:
            # 这里捕获所有会产生的异常，并打印进日志
            logging.error('没连上这个服务器')
        return new_std_out,new_std_err



    def main(self, cmd, method, thread_num=1):
        '''
        最终实现逻辑的主函数
        '''
        # 获取最终存在的服务器更新列表
        self.update_hosts = self.get_exists_host()
        try:
            # linux命令行上执行时输出打印信息（让脚本使用者能看的清楚明了）
            r = raw_input('本次需要更新以下服务器：{},服务器数量：{}，服务器更新命令：{}，确认按1：'.format(self.host_lists,len(self.update_hosts),cmd))
            # 判断用户输入是否合法，输入不合法退出程序
            if len(r) ==  1 and r.isdigit() and int(r) == 1:
                    pass
            else:
                return False
        except:
            print
            return False
        obj_dict = dict()
        total_host = len(self.update_hosts)
        current_hostname = 1
        # 进度条相关处理，具体用法可以参见http://www.cnblogs.com/hongfei/p/3982259.html(这个讲的比较好，还有动图)
        progress = ProgressBar()
        proceed_progress = progress(range(total_host))

# 多线程相关处理，具体用法可以参见
# 这里创建了线程池，max_workers是默认的处理线程个数
# 参见https://docs.python.org/3/library/concurrent.futures.html
with futures.ThreadPoolExecutor(max_workers=int(thread_num)) as executor:
    for hostname in self.update_hosts:
        # 得到异步提交的future对象(也就是executor)的结果
        e = executor.submit(method,hostname,cmd)
        # 生成对象结果与主机名相对应的字典
        obj_dict[e] = hostname

    # concurrent.futures.as_completed返回了一个迭代器，yield那些完成的futures对象
    # 任何futures在调用as_completed()之前完成首先被yield。
    # 参见https://docs.python.org/3/library/concurrent.futures.html
    for future in futures.as_completed(obj_dict):
        # 从futures.as_completed返回的迭代器中获取主机名字
        host_name = obj_dict[future]
        # 捕获异常
        if future.exception() is not None:
            logging.error('generated an exception: %s' % (future.exception()))
        else:
            # 获取结果
            n , e = future.result()
            # 日志里打印实时进度
            logging.info('percent: {1:0.2f}%,  excuting host: {0} '.format(host_name,(current_hostname/float(total_host))*100))
            # 每循环一次，进度条走一格
            proceed_progress.__next__()
            # 用于显示实时脚本执行进度
            current_hostname += 1
        try:
            # 进度条结束，捕获迭代异常
            proceed_progress.__next__()
        except StopIteration:
            # linux命令行上输出换一行，显得美观
            print




if __name__ == '__main__':
    generate_obj = run()
    # 生成参数对象（argparse模块）
    args = generate_obj.argument()
    # 执行主函数部分（分别给主函数传入：命令行获取到的参数，ssh方法，命令行获取线程数参数）
    generate_obj.main(args.cmd_value, generate_obj.remote_ssh, args.num_value)