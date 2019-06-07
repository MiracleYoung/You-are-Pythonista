import functools
d_fun={}

def register(fn):
    d_fun.update({fn.__name__:fn})
    @functools.wraps(fn)
    def wrap(*args, **kwargs):
        #d_fun.update({fn.__name__:fn})
        ret = fn(*args, **kwargs)
        return ret
    return wrap

def cmd():
    end = 'exit'
    while True:
        c = input('>>请输入命令:')
        if c==end:
            break
        if c in d_fun:
            para = input('>>请输入参数:')
            s_para = para.split(',')
            t = []
            for x in s_para:
                t.append(int(x))
            print('>>结果:',d_fun[c](*t))
        else:
            print('?没有此条命令o')
@register
def add(x,y):
    return x+y
@register
def multi(x,y):
    return x*y

cmd()