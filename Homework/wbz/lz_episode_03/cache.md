#### 写一个cache装饰器，允许过期。当某个函数被cache装饰器装饰过后，在过期时间内重复调用它，是返回的缓存结果，而不是去重新计算。
```
# 先在本地建2个空的文本文件，result.txt 和 time.txt

import datetime

def cache(s,curr_time = datetime.datetime.now()):
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

                delta = curr_time - datetime.datetime.strptime(content_time,'%Y-%m-%d %H:%M:%S')
                delta_s = delta.seconds

                if delta_s < s:
                    with open('result.txt', 'r+') as fr:
                        content = fr.read()
                        return content
                else:
                    ret = fn(a,b)
                    with open('result.txt', 'w+') as fr:
                        fr.write(str(ret))
                    return ret
        return wrap
    return _cache

@cache(30)
def add(a,b):
    return a+b


print(add(4,7))
```
