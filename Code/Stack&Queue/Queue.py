# coding:utf-8
import Data_Structure.LinkList.SingleLinkList as SLL
import Data_Structure.LinkList.SingleCycleLinkList as SCL
import Data_Structure.LinkList.DoubleLinkList as DLL
import Data_Structure.LinkList.DoubleCycleLinkList as DCL


# You need to download:
# /code/LinkList/SingleLinkList.py
# /code/LinkList/SingleCycleLinkList.py
# /code/LinkList/DoubleLinkList.py
# /code/LinkList/DoubleCycleLinkList.py
# and import LinkList classes in them

class Queue(object):
    """队列 Queue"""

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        """Remove an element from the head of the queue"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        """Determine whether a queue is empty"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        """Returns the size of the queue"""
        return len(self.__list)


class SingleLinkListQueue(SLL.SingleLinkList):
    """单链表队列: 尾部进头部出"""
    """Single Link List Queue: Tail in and head out"""

    def __init__(self):
        super(SingleLinkListQueue, self).__init__()

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        """Remove an element from the head of the queue"""
        if self.is_empty():
            return None
        else:
            # cursor points to head
            cur = self.head()
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


class SingleCycleLinkListQueue(SCL.SingleCycleLinkList):
    """单链表循环队列: 尾部进头部出"""
    """Single Cycle Link List Queue: Tail in and head out"""

    def __init__(self):
        super(SingleCycleLinkListQueue, self).__init__()

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        """Remove an element from the head of the queue"""
        if self.is_empty():
            return None
        else:
            # cursor points to head
            cur = self.head()
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


class DoubleLinkListQueue(DLL.DoubleLinkList):
    """双向链表队列: 尾部进头部出"""
    """Double Link List Queue: Tail in and head out"""

    def __init__(self):
        super(DoubleLinkListQueue, self).__init__()

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        """Remove an element from the head of the queue"""
        if self.is_empty():
            return None
        else:
            # cursor points to head
            cur = self.head()
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


class DoubleCycleLinkListQueue(DCL.DoubleCycleLinkList):
    """双向循环链表队列: 尾部进头部出"""
    """Double Cycle Link List Queue: Tail in and head out"""

    def __init__(self):
        super(DoubleCycleLinkListQueue, self).__init__()

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        """Add an item element to the queue"""
        self.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        """Remove an element from the head of the queue"""
        if self.is_empty():
            return None
        else:
            # cursor points to head
            cur = self.head()
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
    # ========= test =========
    s = DoubleLinkListQueue()
    print(s.is_empty())  # True
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    s.enqueue(5)
    s.enqueue(6)  # 1 2 3 4 5 6
    print(s.is_empty())  # False
    print("size:", s.size())  # 6
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.is_empty())  # True
    print("size:", s.size())  # 0

    # ====== Result ===== #
    #                     #
    # True                #
    # False               #
    # size: 6             #
    # 5                   #
    # 2                   #
    # 6                   #
    # 4                   #
    # 1                   #
    # 3                   #
    # True                #
    # size: 0             #
    # =================== #
