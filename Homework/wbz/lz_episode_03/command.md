```
import functools

fun_List = []

def register(fn):
    global  fun_List
    fun_List.append(fn)
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        ret = fn(*args,**kwargs)
        return ret
    return wrapper

@register
def add(x,y):
    return int(x) + int(y)

@register
def test(x):
    return x

while True:
    fun_name = input('>>输入指令：')
    if fun_name == 'q':
        print('退出')
        break
    result = 'default'
    for fn in fun_List:
        if fun_name == fn.__name__:
            args = input('>>输入参数：')
            args_list = args.split(',')
            result = fn(*args_list)
            break

    print('>>结果',result)
 ```
    ![image](https://github.com/wubaozhen/You-are-Pythonista/blob/master/Homework/wbz/lz_episode_03/03_02.PNG)
