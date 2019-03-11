#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/3/9 9:29 PM

__author__ = 'Miracle'

import snowboydecoder
import sys
import signal

# 全局变量
# TODO: 解释下干嘛的
interrupted = False


def signal_handler(signal, frame):
    '''
    :param signal: TODO 这2个参数又是干嘛的，什么时候用的
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

# TODO：这一步在干嘛？
signal.signal(signal.SIGINT, signal_handler)

# TODO：这一步又在干嘛？
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.3)
print('Listening... Press Ctrl+C to exit')

# 函数主体循环
# TODO：detected_callback作用
# TODO：interrupt_check作用
# TODO：sleep_time作用
detector.start(detected_callback=snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03
               )

detector.terminate()
