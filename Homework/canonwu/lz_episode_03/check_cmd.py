from functools import wraps
func_list=[]
def register(func):
    func_list.append(func)
    print("{} 是一个注册的函数".format(func.__name__))
    @wraps(func)
    def wrap(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return wrap

@register
def add(x,y):
    try:
        x=int(x)
        y=int(y)
    except TypeError:
        raise TypeError('x, y must be int type')
    return x+y

@register
def multi(x,y):
    try:
        x=int(x)
        y=int(y)
    except TypeError:
        raise TypeError('x, y must be int type')
    return x*y

if __name__ == '__main__':
    quit = 'quit'
    while True:
        cmd = input('>>请输入命令:')
        if cmd == quit:
            break
        for func in func_list:
            if cmd == func.__name__:
                param = input('>>请输入参数，并用\',\'隔开:')
                params = param.split(',')
                if len(params) != 2:
                    raise ValueError('只能输入2位参数！')
                else:
                    print('>>结果:', func(*params))
            else:
                print('没有这个命令！')
