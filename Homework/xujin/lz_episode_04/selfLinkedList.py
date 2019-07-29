
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

class LinkedList():
    def __init__(self):
        # 头
        self.head = None

    def __find_tail(self):
        current = self.head
        while current.next is not None:
            current = current.next
        return current

    def append(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            # 得到尾节点
            tail = self.__find_tail()
            tail.next = node

    def pop(self):
        if self.head is None:
            return None

        current = self.head
        temp = None
        while current.next is not None:
            temp = current
            current = current.next

        if temp is None:
            self.head = None
        else:
            temp.next = None
        return current.value

    def insert(self,index,value):
        '''
        插入一个数据，index指定插入的位置，下标从零开始
        :param index: 插入位置，>= 0
        :param value: 插入的值
        :return:
        '''
        node = Node(value)
        previous_node = None
        if index < 0:
            raise ValueError(f'{index} must greater than 0 or equal to 0')

        if index == 0:
            node.next = self.head
            self.head = node
            return

        current = self.head

        if current is None:
            raise ValueError(f'linkList length is 0,but index is {index},out of linkList length')

        current_index = 0
        while current.next is not None:
            previous_node = current
            current = current.next
            current_index += 1
            if current_index == index:
                previous_node.next = node
                node.next = current
                return

        if current_index+1 == index:
            current.next = node
            node.next = None
            return

        raise ValueError(f'linkList length is {current_index + 1},but index is {index},out of linkList length')

    def remove(self,index):
        '''
        根据下标删除一个节点  下标从零开始
        :param index:
        :return:
        '''
        if index < 0:
            raise ValueError(f'{index} must greater than 0 or equal to 0')

        if self.head is None:
            raise ValueError('linkList is None,can`t remove node')

        previous = None
        current = self.head
        current_index = 0

        if index == 0:
            self.head = current.next
            return

        while current.next is not None:
            previous = current
            current = current.next
            current_index += 1
            if current_index == index:
                previous.next = current.next
                return

        if current_index <= index:
            raise ValueError(f'linkList length is {current_index},but params index is {index},out of list')

    def show_data(self):
        if self.head is None:
            print(None)
        else:
            current = self.head
            data = [str(current)]
            while current.next is not None:
                current = current.next
                data.append(str(current))

            print("->".join(data))

if __name__=='__main__':
    links = LinkedList()
    links.append('xujin')
    links.append('yangling')
    links.append('liailing')
    links.insert(2,'test')
    links.insert(0,'one')
    links.insert(5,'last')
    links.show_data()

    print(links.pop())
    links.show_data()

    links.remove(3)
    links.show_data()
    links.insert(4,'last')
    links.show_data()
    links.insert(5,'finally')
    links.show_data()

    # 另外一个文件中
    # node_str = 'Node'
    # package = __import__('file_name')
    # node = getattr(package,node_str)

    # node = eval('Node("test")')
    # print(type(node))

