#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/4/24 6:52 AM

__author__ = 'Miracle'

'''
初始代码
'''
# 首先要有一个列表, 槽位, 需要初始化
slots = []
# 假设给他32个槽位数
slots_num = 32

# 这个是用来初始化我们的槽位
for _ in range(slots_num):
    slots.append([])


# 我们的put方法, 就是把key put到value里面
def put(slots, key, value):
    # 先得到它的索引, 就是我们的槽位数取模, 这样就得到了它的索引值了
    i = hash(key) % slots_num
    # 把它的k-v对通过远组的方式put进去
    slots[i].append((key, value))


# get方法
def get(slots, key):
    # 首先求出它的i, 还是hash取模
    i = hash(key) % slots_num
    # 得到之后呢, 对他进行循环
    for k, v in slots[i]:
        if k == key:
            return v
    # 最后没有取到呢, 就会抛出异常
    raise KeyError(k)


'''
被优化过的代码
'''

slots = []
slots_num = 32

for _ in range(slots_num):
    slots.append([])


def put(slots, key, value):
    i = hash(key) % slots_num

    # 现在我们不能再简单的append了, 需要判断下, 需要记录一下他的位置
    # 所以用enumerate, 还记得这个内置函数吗？
    # 这里就用到了解构，不记得的可以回看一下
    for p, (k, v) in enumerate(slots[i]):
        if k == key:
            break
    # 如果没有相同的, 才append
    else:
        slots[i].append((key, value))
        return

    # 如果p>=0，说明某个槽位被占用了，因为0才是第一位，
    if p >= 0:
        slots[i][p] = (key, value)


def get(slots, key):
    i = hash(key) % slots_num
    for k, v in slots[i]:
        if k == key:
            return v
    raise KeyError(k)


'''
至于类的写法, 大家有可能不知道怎么写的, 我们简单的看看
'''


class Dict:
    # 初始化需要一个num, 用来定义槽位数
    def __init__(self, num):
        self.__slots__ = []
        self.num = num
        # 这里又看到 _ 了吧, 在for循环里
        # 我们不需要这个num具体的每一个值吧, 我们只需要初始化列表
        for _ in range(num):
            self.__slots__.append([])

    # 我们把上面的put和get直接搬下来就ok了, 然后稍作修改
    def put(self, key, value):
        # 需要修改几个地方
        # slots_num -> self.num
        # slots[i] -> self.__slots__[i]
        i = hash(key) % self.num
        for p, (k, v) in enumerate(self.__slots__[i]):
            if k == key:
                break
        else:
            self.__slots__[i].append((key, value))
            return
        self.__slots__[i][p] = (key, value)

    def get(self, key):
        i = hash(key) % self.num
        for k, v in self.__slots__[i]:
            if k == key:
                return v
        raise KeyError(key)

    # 所以我们只要多一个遍历函数就好了
    def keys(self):
        ret = []
        for slot in self.__slots__:
            for k, _ in slot:
                ret.append(k)
        return ret
