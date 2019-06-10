# -*- coding: utf-8 -*-


# 将被装饰器注册过的函数放入字典
func_dict = dict()


def register(func):
    # 直接将函数放入字典 解决未调用函数无法添加到字典的问题
    func_dict[func.__name__] = func

    def wrap(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return wrap


@register
def add(x, y):
    return x + y


@register
def sub(x, y):
    return x - y


@register
def divide(x, y):
    return x / y


@register
def mult(x, y):
    return x * y


def default():
    print('>>deult,该指令未定义。。。')


def main():
    while True:
        cmd = input('>>请输入指令：(输入exit退出)\n')
        if cmd in func_dict.keys():
            params = input('>>请输入两个参数以逗号分隔：\n').split(',')
            ret = func_dict[cmd](int(params[0]), int(params[1]))
            print(ret)
        elif cmd == 'exit':
            exit()
        else:
            default()


if __name__ == '__main__':
    main()
