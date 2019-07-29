"""
命令份发器
通过交互的方式让用户输入指令，如果某个函数被注册过，那么在交互模式中输入调用该函数，是可以运行出结果的，如果没有，则返回默认函数。
"""
# 注册函数字典
register_dic = {}


def register(func, *args, **kwargs):
    register_dic.setdefault(func.__name__, (func, func.__code__.co_argcount))

    def _reg(*args, **kwargs):
        return func(*args, **kwargs)
    return _reg


@register
def add(x: int, y: int, z: int) -> int:
    if x.isdigit() and y.isdigit() and z.isdigit():
        return x + y + z
    print("传递参数有误")


@register
def sub(x: int, y: int)->int:
    if x.isdigit() and y.isdigit():
        return x - y
    print("传递参数有误")


def mul(x: int, y: int)->int:
    if x.isdigit() and y.isdigit():
        return x * y
    print("传递参数有误")


@register
def default():
    return "default"


def main():
    menu = ">>> 输入指令 (按 q 退出)："
    menu_params = ">>> 输入参数({}个, 多个参数使用 ',' 分隔)："
    menu_realut = ">>> 结果: {}"
    while True:
        instruction = input(menu)
        if instruction in "qQ":
            print("\nByebye~~")
            break
        if register_dic.get(instruction):
            if register_dic[instruction][1]:
                params = input(menu_params.format(
                    register_dic[instruction][1]))
                params = [i.strip() for i in params.split(",") if i.strip()]
                if len(params) == register_dic[instruction][1]:
                    reault = register_dic[instruction][0](*params)
                else:
                    print("输入参数个数有误!")
                    continue
        else:
            reault = register_dic["default"][0]()
        if reault:
            print(menu_realut.format(reault))


if __name__ == "__main__":
    # print(register_dic)
    main()
    """结果:
        >>> 输入指令 (按 q 退出)：add
        >>> 输入参数(3个, 多个参数使用 ',' 分隔)：3, 45, 1
        >>> 结果: 49
        >>> 输入指令 (按 q 退出)：sub
        >>> 输入参数(2个, 多个参数使用 ',' 分隔)：93, 23
        >>> 结果: 70
        >>> 输入指令 (按 q 退出)：qwe
        >>> 结果: default
        >>> 输入指令 (按 q 退出)：q

        Byebye~~
    """
