#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/3/9 9:29 PM

__author__ = 'Miracle'

import snowboydecoder
import sys
import signal

# 全局变量
# 防止并发，本篇文章先做单线程处理
interrupted = False


def signal_handler(signal, frame):
    '''
    定义一个信号处理函数，该函数将接收所有信号
    :param signal: 信号
    :param frame:
    :return:
    '''
    global interrupted
    interrupted = True


def interrupt_callback():
    '''
    TODO：callback在什么时候会被触发
    '''
    global interrupted
    return interrupted


# 检查参数，程序必须接受一个模型文件
if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# SIGINT：连接中断信号，设置处理的handler
signal.signal(signal.SIGINT, signal_handler)

# 主程序在这里执行，sleep_time=0.03 秒
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.3)
print('Listening... Press Ctrl+C to exit')

# 函数主体循环
# detected_callback：检查填充有麦克风数据的环形缓冲区，以查看是否检测到一个唤醒词，如果是则触发该函数
# interrupt_check：如果它返回True，则断开主循环并返回
detector.start(detected_callback=snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03
               )

detector.terminate()
