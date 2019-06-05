import functools

func_list = []

def register(func):
    global func_list
    func_list.append(func)
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
    return wrapper

@register
def add(x,y):
    try:
        x = int(x)
        y = int(y)
    except:
        pass
    return x+y

@register
def test(x):
    return x

if __name__ == '__main__':
    print("输入q退出命令模式")
    while True:
        cmd = input(">> 输入指令:")
        result = "default"
        if cmd == 'q':
            break
        for func in func_list:
            if cmd == func.__name__:
                args = input(">> 请输入参数,多个参数之间用','隔开:").split(',')
                result = func(*args)
                break

        print(">> 结果：",result)

