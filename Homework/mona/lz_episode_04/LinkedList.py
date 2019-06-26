class Node:
    def __init__(self, element, prev=None, next = None):
        self.element = element
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.__size = 0

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def insert(self, x):
        self.__insert(x, self.__size)

    def __insert(self, x, id):
        t = self.head
        for _ in range(id):
            t = t.next

        newNode = Node(x, t, t.next)

        t.next.prev = newNode
        t.next = newNode
        self.__size = self.__size + 1

    def delete(self, x):
        self.__delete(x)

    def __delete(self, x):
        t = self.head.next
        while (t != self.tail):
            if (t.element == x):
                t.next.prev = t.prev
                t.prev.next = t.next
                print('You have deleted the element {}.'.format(x))
                return
            t  = t.next

        print('There is no element {} in the list'.format(x))

    def contains(self, x):
        t = self.head.next
        while (t != self.tail):
            if (t.element == x):
                return True

        return False

    def show(self):
        t = self.head.next
        print('The elements in this list:',end='')
        while (t != self.tail):
            print(t.element, end=' ')
            t = t.next
        print()

link = LinkedList()

link.insert(1)
link.insert(2)
print('The size of this list is {}.'.format(link.size()))
link.insert('haah')
print('The size of this list is {}.'.format(link.size()))
link.show()
link.delete(2)
link.delete(2)