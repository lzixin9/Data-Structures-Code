import Data_Structure.LinkList.SingleLinkList as SLL
import Data_Structure.LinkList.SingleCycleLinkList as SCL
import Data_Structure.LinkList.DoubleLinkList as DLL
import Data_Structure.LinkList.DoubleCycleLinkList as DCL


# you need change the "01_SingleLinkList单链表.py"..."04_..." to "SingleLinkList.py"... first
# The above code can be modified and imported according to the location of the link list py file


class ListDeque(object):
    """列表双端队列"""
    """List Dequeue"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.__list.append(item)

    def pop_front(self):
        """从队列头部删除一个元素"""
        """Remove an element from the head of the queue"""
        return self.__list.pop(0)

    def pop_rear(self):
        """从队列尾部删除一个元素"""
        """Remove an element from the end of the queue"""
        return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        """Determine whether a queue is empty"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        """Returns the size of the queue"""
        return len(self.__list)


class SingleLinkListDeque(SLL.SingleLinkList):
    """单链表双端队列"""
    """Single Link List Dequeue"""

    def __init__(self):
        super(SingleLinkListDeque, self).__init__()

    def add_front(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.add(item)

    def add_rear(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.append(item)

    def pop_front(self):
        """从队列头部删除一个元素"""
        """Remove an element from the head of the queue"""
        if self.is_empty():
            return None
        else:
            # cursor points to head
            cur = self.head()
            self.remove(cur.elem)
            return cur.elem

    def pop_rear(self):
        """从队列尾部删除一个元素"""
        """Remove an element from the end of the queue"""
        if self.is_empty():
            return None
        else:
            # cursor 游标
            cur = self.head()
            pre = None
            # travel
            while cur.next is not None:
                pre = cur
                cur = cur.next
            # 退出循环，cur指向尾节点 Exit the loop, "cur" points to the tail node
            # 删除尾节点 delete the tail node
            if self.length() != 1:
                # The number of nodes is not 1
                pre.next = None
            else:
                # The number of nodes is 1
                self.remove(cur.elem)
            return cur.elem

    def is_empty(self):
        """判断一个队列是否为空"""
        """Determine whether a queue is empty"""
        return not self.head()

    def size(self):
        """返回队列的大小"""
        """Returns the size of the queue"""
        return self.length()


class SingleCycleLinkListDeque(SCL.SingleCycleLinkList):
    """单向循环链表双端队列"""
    """Single Cycle Link List Dequeue"""

    def __init__(self):
        super(SingleCycleLinkListDeque, self).__init__()

    def add_front(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.add(item)

    def add_rear(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.append(item)

    def pop_front(self):
        """从队列头部删除一个元素"""
        """Remove an element from the head of the queue"""
        if self.is_empty():
            return None
        else:
            # cursor points to head
            cur = self.head()
            self.remove(cur.elem)
            return cur.elem

    def pop_rear(self):
        """从队列尾部删除一个元素"""
        """Remove an element from the end of the queue"""
        if self.is_empty():
            return None
        else:
            # cusor 游标
            # 保留头节点地址 save the head's address
            head = self.head()
            cur = self.head()
            pre = None
            # travel to the tail
            while cur.next is not head:
                pre = cur
                cur = cur.next
            # 退出循环，cur指向尾节点 Exit the loop, "cur" points to the tail node
            if self.length() != 1:
                # points to the head node
                pre.next = head
            else:
                self.remove(cur.elem)
            return cur.elem

    def is_empty(self):
        """判断一个队列是否为空"""
        """Determine whether a queue is empty"""
        return not self.head()

    def size(self):
        """返回队列的大小"""
        """Returns the size of the queue"""
        return self.length()


class DoubleLinkListDeque(DLL.DoubleLinkList):
    """双向链表双端队列"""
    """Double Link List Dequeue"""

    def __init__(self):
        super(DoubleLinkListDeque, self).__init__()

    def add_front(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.add(item)

    def add_rear(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.append(item)

    def pop_front(self):
        """从队列头部删除一个元素"""
        """Remove an element from the head of the queue"""
        if self.is_empty():
            return None
        else:
            # cursor points to head
            cur = self.head()
            self.remove(cur.elem)
            return cur.elem

    def pop_rear(self):
        """从队列尾部删除一个元素"""
        """Remove an element from the end of the queue"""
        if self.is_empty():
            return None
        else:
            if self.is_empty():
                return None
            else:
                # cusor 游标
                cur = self.head()
                # travel
                while cur.next is not None:
                    cur = cur.next
                # 退出循环，cur指向尾节点 Exit the loop, "cur" points to the tail node
                if cur.prev is not None:
                    cur.prev.next = None
                else:
                    self.remove(cur.elem)
                return cur.elem

    def is_empty(self):
        """判断一个队列是否为空"""
        """Determine whether a queue is empty"""
        return not self.head()

    def size(self):
        """返回队列的大小"""
        """Returns the size of the queue"""
        return self.length()


class DoubleCycleLinkListDeque(DCL.DoubleCycleLinkList):
    """双向循环链表双端队列"""
    """Double Cycle Link List Dequeue"""

    def __init__(self):
        super(DoubleCycleLinkListDeque, self).__init__()

    def add_front(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.add(item)

    def add_rear(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.append(item)

    def pop_front(self):
        """从队列头部删除一个元素"""
        """Remove an element from the head of the queue"""
        if self.is_empty():
            return None
        else:
            # cursor points to head
            cur = self.head()
            self.remove(cur.elem)
            return cur.elem

    def pop_rear(self):
        """从队列尾部删除一个元素"""
        """Remove an element from the end of the queue"""
        if self.is_empty():
            return None
        else:
            # cusor
            cur = self.head()
            # travel
            while cur.next != self.head():
                cur = cur.next
            # 退出循环，cur指向尾节点 Exit the loop, "cur" points to the tail node
            if cur.prev is not None:
                cur.prev.next = self.head()
            else:
                self.remove(cur.elem)
            return cur.elem

    def is_empty(self):
        """判断一个队列是否为空"""
        """Determine whether a queue is empty"""
        return not self.head()

    def size(self):
        """返回队列的大小"""
        """Returns the size of the queue"""
        return self.length()


if __name__ == "__main__":
    s = DoubleCycleLinkListDeque()
    print(s.is_empty())  # True
    s.add_front(1)
    s.add_front(2)  # 2 1
    s.add_rear(3)
    s.add_rear(4)  # 2 1 3 4
    s.add_front(5)
    s.add_rear(6)  # 5 2 1 3 4 6
    print(s.is_empty())  # False
    print("size:", s.size())  # 6
    print(s.pop_front())  # 5
    print(s.pop_front())  # 2
    print(s.pop_rear())  # 6
    print(s.pop_rear())  # 4
    print(s.pop_front())  # 1
    print(s.pop_rear())  # 3
    print(s.is_empty())  # True
    print("size:", s.size())  # 0
