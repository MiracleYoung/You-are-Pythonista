"""
实现一个LinkedList 链表,https://www.cnblogs.com/jiuyang/p/7930470.html
"""


# node 结点//链表节点结构实现  私有属性_pro_item是指向下个节点的指针，_item为此节点的值
class Node:

    def __init__(self, item=None, pos_item=None):

        self.item = item
        self.next = pos_item

    def __repr__(self):
        """
        用来定义Node的字符输出，
        print为输出item
        """
        return str(self.item)


# 单链表实现
class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    # 判空
    def is_empty(self):
        return self.length == 0

    # 链表结尾插入
    def append(self, item):

        if isinstance(item, Node):
            node = item
        else:
            node = Node(item)

        if self.head is None:
            self.head = node
        else:
            be_node = self.head
            while be_node.next:
                be_node = be_node.next
            be_node.next = node
        self.length += 1


    # 插入数据
    def insert(self, index, item):

        if self.is_empty():
            print('This LinkedList is empty.')
            return

        if index < 0 or index >= self.length:
            print("error: out of index")
            return

        in_node = Node(item)
        node = self.head
        count = 1

        while True:
            node = node.next
            count += 1
            if count == index:

                next_node = node.next
                node.next = in_node
                in_node.next = next_node
                self.length += 1
                return

    # 删除数据
    def delete(self, index):

        if self.is_empty():
            print('This LinkedList is empty')
            return

        if index < 0 or index >= self.length:
            print("error: out of index")
            return
        # if index == 0
        #     self._head = None
        else:
            node = self.head
            count = 0
            while True:
                count += 1
                if index == count:
                    node.next = node.next.next
                    break
                node = node.next

        self.length -= 1

    def __repr__(self):
        if self.is_empty():
            print("This LinkedList is empty")
            return
        n_list = ""
        node = self.head
        while node:
            n_list += node.item + ''
            node = node.next
        return n_list


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.append('A')
    linkedList.append('B')
    linkedList.append('C')
    linkedList.append('D')
    linkedList.append('E')
    linkedList.append('F')
    linkedList.append('G')
    print('Raw   linkedList is: ', linkedList)
    linkedList.insert(4, 'p')
    print('New   linkedList is: ', linkedList)
    linkedList.delete(3)
    print('Final linkedList is: ', linkedList)
    print('Head of linkedList is: ', linkedList.head.item)
    print('Length of linkedList is: ', linkedList.length)

