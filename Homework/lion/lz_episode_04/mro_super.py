# -*- coding: utf-8 -*-
from types import MethodType


# 遍历某个类型的所有父类 检测是否存在该方法 如果存在 使用getattr取出并返回方法 完成调用
class Super:
    # type: 查找mro的类 obj:
    def __init__(self, type, obj):
        self.type = type
        self.obj = obj

    def __getattr__(self, name):  # 要寻找的方法的名称
        is_father = False  # 标记是否为父类
        for cls in self.type.__mro__:
            if hasattr(cls, name) and is_father:
                # 第一次找到的是自身类型中的方法 不是父类里面的
                return MethodType(getattr(cls, name), self.obj)
            if cls == self.type:
                is_father = True  # 已经跳过了自身类型
        raise AttributeError  # 没有找到这个方法


class A:
    def eat(self):
        print('something can be  eaten')


class B(A):
    def eat(self):
        # a = MethodType(getattr(A, 'eat'), A)
        Super(B, self).eat()
        print("son's eat")


if __name__ == '__main__':
    b = B()
    b.eat()
