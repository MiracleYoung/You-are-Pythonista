#### 写一个cache装饰器，允许过期。当某个函数被cache装饰器装饰过后，在过期时间内重复调用它，是返回的缓存结果，而不是去重新计算。
```
# 先在本地建2个空的文本文件，result.txt 和 time.txt
import datetime
import time

def cache(s):
    def _cache(fn):
        def wrap(a,b):
            with open('result.txt','r+') as fr:
                content = fr.read()
            if not content:
                ret = fn(a,b)
                with open('result.txt', 'w+') as fr:
                    fr.write(str(ret))
                time = datetime.datetime.now().strftime( '%Y-%m-%d %H:%M:%S')
                with open('time.txt', 'w+') as ft:
                    ft.write(time)
                return ret
            else:
                with open('time.txt', 'r+') as ft:
                    content_time = ft.read()
                curr_time = datetime.datetime.now().strftime('%S')  # 取当前时间的秒
                delta_s = int(curr_time) - int(content_time[-2:])  # 当前时间的秒减去从time.txt里读到的时间
                if delta_s < s:
                    print('还在缓存期内，返回缓存中的值！')
                    with open('result.txt', 'r+') as fr:
                        content = fr.read()
                        return content
                else:
                    print('已超过缓存时间，将重新计算！')
                    ret = fn(a,b)
                    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    with open('time.txt', 'w+') as ft:
                        ft.write(time)
                    with open('result.txt', 'w+') as fr:
                        fr.write(str(ret))
                    return ret
        return wrap
    return _cache

@cache(10)
def add(a,b):
    return a+b


print(add(4,7))
time.sleep(5)
print(add(4,8))
time.sleep(20)
print(add(4,9))                  
```
![image](https://github.com/wubaozhen/You-are-Pythonista/blob/master/Homework/wbz/lz_episode_03/03_01.PNG)
