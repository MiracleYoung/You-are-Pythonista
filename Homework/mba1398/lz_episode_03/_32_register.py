import functools
d_fun = {}


def register(fn):
    # print(fn)
    # 字典可以update，列表不能，只能设置全局变量？
    d_fun.update({fn.__name__: fn})
    # print(d_fun)
    @functools.wraps(fn)
    def wrap(*args, **kwargs):
        ret = fn(*args, **kwargs)
        return ret
    return wrap


# 外部传入变量的名字和函数内部的名称一致会提示错误，不建议这样
@register
def add(x, y):
    return x+y


@register
def multi(x, y):
    return x*y


if __name__ == '__main__':
    end = 'q'
    while True:
        c = input('>>Please input your command: ')
        if c == end:
            break
        if c in d_fun:
            para = input(">>Please input 2 parameters,split by ',': ")
            paras = para.split(',')
            # print(paras)
            print('>>The result is: ', d_fun[c](int(paras[0]), int(paras[1])))
            # t = []
            # for i in paras:
            #     # 字符转换为int
            #     t.append(int(i))
            # print(t, c, d_fun[c])
            # *t直接传入可变位置参数
            # print('>>结果:', d_fun[c](*t))
        else:
            print('There is no this command!')
