# coding:utf-8
import Data_Structure.LinkList.SingleCycleLinkList as SCL
import Data_Structure.LinkList.DoubleLinkList as DLL
import Data_Structure.LinkList.DoubleCycleLinkList as DCL


# You need to download:
# /code/LinkList/SingleLinkList.py
# /code/LinkList/SingleCycleLinkList.py
# /code/LinkList/DoubleLinkList.py
# /code/LinkList/DoubleCycleLinkList.py
# and import LinkList classes in them


class ListStack(object):
    """列表栈"""
    """List Stack"""

    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        """Add a new element item to the top of the stack"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        """Pop the top element"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        """Return the top element of the stack"""
        if self.__list:
            # List is not empty 列表不为空
            return self.__list[-1]
        else:
            # List is empty 列表为空
            return None

    def is_empty(self):
        """判断栈是否为空"""
        """Determine whether the stack is empty"""
        return not self.__list

    def size(self):
        """返回栈的元素个数"""
        """Returns the number of elements in the stack"""
        return len(self.__list)


class SingleLinkListStack(SLL.SingleLinkList):
    """单链表栈"""
    """Single Link List Stack"""

    def __init__(self):
        super(SingleLinkListStack, self).__init__()

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        """Add a new element item to the top of the stack"""
        self.append(item)

    def pop(self):
        """弹出栈顶元素"""
        """Pop the top element"""
        if self.is_empty():
            return None
        else:
            # cursor
            # 游标
            cur = self.head()
            pre = None
            # travel
            while cur.next is not None:
                pre = cur
                cur = cur.next
            # 退出循环，cur指向尾节点  Exit the loop, "cur" points to the tail node
            # 删除尾节点  delete the tail node
            if self.length() != 1:
                # The number of nodes is not 1
                pre.next = None
            else:
                # The number of nodes is 1
                self.remove(cur.elem)
            return cur.elem

    # 已继承，无需重写 it has been inherited, no need to rewrite
    def is_empty(self):
        """判断栈是否为空"""
        """Determine whether the stack is empty"""
        return not self.head()

    def size(self):
        """返回栈的元素个数"""
        """Returns the number of elements in the stack"""
        return self.length()


class SingleCycleLinkListStack(SCL.SingleCycleLinkList):
    """单向循环链表栈"""
    """Single Cycle Link List Stack"""

    def __init__(self):
        super(SingleCycleLinkListStack, self).__init__()

    def is_empty(self):
        """判断栈是否为空"""
        """Determine whether the stack is empty"""
        return not self.head()

    def size(self):
        """返回栈的元素个数"""
        """Returns the number of elements in the stack"""
        return self.length()

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        """Add a new element item to the top of the stack"""
        self.append(item)

    def pop(self):
        """弹出栈顶元素"""
        """Pop the top element"""
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


class DoubleLinkListStack(DLL.DoubleLinkList):
    """双向链表栈"""
    """Double Link List Stack"""

    def __init__(self):
        super(DoubleLinkListStack, self).__init__()

    def is_empty(self):
        """判断栈是否为空"""
        """Determine whether the stack is empty"""
        return not self.head()

    def size(self):
        """返回栈的元素个数"""
        """Returns the number of elements in the stack"""
        return self.length()

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        """Add a new element item to the top of the stack"""
        self.append(item)

    def pop(self):
        """弹出栈顶元素"""
        """Pop the top element"""
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


class DoubleCycleLinkListStack(DCL.DoubleCycleLinkList):
    """双向循环链表栈"""
    """Double Cycle Link List Stack"""

    def __init__(self):
        super(DoubleCycleLinkListStack, self).__init__()

    def is_empty(self):
        """判断栈是否为空"""
        """Determine whether the stack is empty"""
        return not self.head()

    def size(self):
        """返回栈的元素个数"""
        """Returns the number of elements in the stack"""
        return self.length()

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        """Add a new element item to the top of the stack"""
        self.append(item)

    def pop(self):
        """弹出栈顶元素"""
        """Pop the top element"""
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


if __name__ == "__main__":
    # ========= test =========
    s = SingleLinkListStack()
    print(s.is_empty())  # True
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)  # 1 2 3 4 5 6
    print(s.is_empty())  # False
    print("size:", s.size())  # 6
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
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
