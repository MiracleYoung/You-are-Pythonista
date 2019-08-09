# 系统编程_15_并行(parallel)和并发（concurrency)?

## Question
并行 (parallel) 和并发（concurrency)?

并行： 同一时刻____同时在运行

不会在同一时刻同时运行，存在交替执行的情况。

实现并行的库有： ____

实现并发的库有:  ____

程序需要执行较多的读写、请求和回复任务的需要大量的 IO 操作，IO 密集型操作使用并发更好。

CPU 运算量大的程序，使用并行会更好

%!A. 多个任务, multiprocessing, threading!%

%!B. 多个任务, threading, multiprocessing!%

%!C. 多个线程, multiprocessing, threading!%

%!D. 多个线程, threading, multiprocessing!%

----

## Answer
@!A!@

----

## Analysis

并行： 同一时刻多个任务同时在运行

不会在同一时刻同时运行，存在交替执行的情况。

实现并行的库有： multiprocessing

实现并发的库有:  threading

程序需要执行较多的读写、请求和回复任务的需要大量的 IO 操作，IO 密集型操作使用并发更好。

CPU 运算量大的程序，使用并行会更好