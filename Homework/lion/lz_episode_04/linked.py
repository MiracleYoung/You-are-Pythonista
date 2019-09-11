# -*- coding: utf-8 -*-


# 节点类
class Node:
    def __init__(self, value):
        # 数据 指针
        self.next = None
        self.value = value


class LinkedList:

    def __init__(self):
        # 头指针永远指向第一个节点 不存放有效数据
        self.head = Node(None)
        # 使用尾指针即当前链表中的最后一个节点
        self.tail = self.head

    def init(self, *args):
        """ 初始化链表 """
        # 链表中的每一个元素都是一个Node类型
        if len(args) != 0:
            for member in args:
                node = Node(member)
                self.tail.next = node
                self.tail = node
        else:
            print("链表为空")

    def is_empty(self):
        if self.head.next is None:
            print('链表为空')
            return True
        else:
            return False

    def show_linked(self):
        """ 显示列表内元素 """
        current_node = self.head
        # 循环内部做判断 当前节点如果为空表明位于最后一个节点的next指针处
        while True:
            current_node = current_node.next
            # None值检测
            if current_node is None:
                return
            print(current_node.value, end='    ')

    def find_index(self, value):
        """ 查找元素索引 """
        if self.is_empty():
            return
        # current_node = self.head.next  # 头指针指向的第一个节点
        # index = 0
        # while current_node.next is not None:  # 当前节点的指针为None表明查找到了最后一个节点
        #     if value == current_node.value:
        #         return index, current_node
        #     else:
        #         index += 1
        #         current_node = current_node.next
        # # 该写法需要单独对最后一个节点做判断
        # if self.tail.value == value:
        #     return index, current_node
        # return '该链表中没有这个元素'
        current_node = self.head
        index = 0
        # 在循环的内部做判断，当前节点为空，位于最后一个节点的next处 直接中止循环
        while True:
            current_node = current_node.next
            if current_node is not None:
                if value == current_node.value:
                    return index, current_node
                index += 1
            else:
                print('链表中没有这个元素')
                return

    def find_value(self, index):
        """ 查找索引处的值 """
        if self.is_empty():
            return
        current_node = self.head
        for _ in range(0, index + 1):
            current_node = current_node.next
            if current_node is None:
                print('给定的索引超出链表长度')
                return
        return current_node

    def add(self, value, index=-1, location=True):
        """ 向链表中添加元素 提供索引 默认在索引位置后插入"""
        if self.is_empty():
            return
        node = Node(value)
        # 索引值为-1直接在元素的尾部插入
        if index != -1:
            if location:  # 后插
                # 查找索引处的节点
                current_node = self.find_value(index)
                # 插入
                node.next = current_node.next
                current_node.next = node
            else:  # 前插
                current_node = self.find_value(index - 1)
                node.next = current_node.next
                current_node.next = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, value):
        if self.is_empty():
            return
        index, current_node = self.find_index(value)
        # 移除当前节点 直接把上一个节点的指针域指向下一个节点
        last_node = self.head
        for i in range(0, index):  # 寻找上一个节点
            last_node = last_node.next
        # 删除操作
        last_node.next = current_node.next
        print('删除完成')

    def update(self, value, index=False):
        """ 修改节点的值 默认按照值查找修改 """
        if self.is_empty():
            return
        try:
            if index:
                node = self.find_value(value)
                new_value = int(input('请输入您要修改的值'))
                node.value = new_value
            else:
                _, node = self.find_index(value)
                new_value = int(input('请输入您要修改的值：'))
                node.value = new_value
        except Exception:
            print('链表中没有这个元素或索引超出范围')


def main():
    # 生成链表
    linked = LinkedList()
    linked.init(1, 2, 3, 4, 6, 7, 10)
    print(f'linked is empty:{linked.is_empty()}')
    print(f"tail pointer's value is {linked.tail.value}")
    linked.show_linked()
    linked.add(11, index=4, location=False)
    print()
    linked.show_linked()
    print()
    linked.update(2, index=True)
    linked.show_linked()
    print()
    linked.find_value(19)
    linked.remove(4)
    print()
    linked.show_linked()
    linked.add(5)
    print()
    linked.show_linked()
    index = linked.find_index(5)
    print()
    print(f'number 5 index is {index[0]}')


if __name__ == '__main__':
    main()
