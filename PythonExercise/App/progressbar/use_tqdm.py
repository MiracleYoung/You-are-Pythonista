#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/8 上午6:07
# @Author  : MiracleYoung
# @File    : tqdm.py

from time import sleep
from tqdm import trange, tqdm
from multiprocessing import Pool, freeze_support, RLock

L = list(range(9))

def progresser(n):
    interval = 0.001 / (n + 2)
    total = 5000
    text = "#{}, est. {:<04.2}s".format(n, interval * total)
    for i in trange(total, desc=text, position=n):
        sleep(interval)

if __name__ == '__main__':
    freeze_support()  # for Windows support
    p = Pool(len(L),
             # again, for Windows support
             initializer=tqdm.set_lock, initargs=(RLock(),))
    p.map(progresser, L)
    print("\n" * (len(L) - 2))