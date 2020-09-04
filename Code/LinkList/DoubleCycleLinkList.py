# coding:utf-8


class Node(object):
    def __init__(self, item):
        """结点"""
        self.elem = item
        self.next = None
        self.prev = None


class DoubleCycleLinkList(object):
    """双向循环链表"""

    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = self.__head

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # 创建游标
        cur = self.__head
        # 计数
        count = 1
        # 循环遍历
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        # 循环结束，cur指向尾节点
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        # 创建游标
        cur = self.__head
        # 循环遍历
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 循环结束，cur指向尾节点
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素，头插法"""
        # 新建节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 新建游标
            cur = self.__head
            # 循环遍历尾节点
            while cur.next != self.__head:
                cur = cur.next
            # 循环结束，cur指向尾节点
            node.next = self.__head
            # 原来的头节点prev指向node
            node.next.prev = node
            self.__head = node
            # 尾节点指向头节点
            cur.next = self.__head

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        # 新建节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 新建游标
            cur = self.__head
            # 循环遍历，找到尾节点
            while cur.next != self.__head:
                cur = cur.next
            # 循环结束，cur指向尾节点
            node.next = self.__head
            node.prev = cur
            # 插入
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param  pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            # 计数
            count = 0
            # 定义游标
            cur = self.__head
            # 创建新增节点
            node = Node(item)
            # 遍历
            while count < pos:  # 这里第一次写出错了，牢记pos与pos-1的区别， pos-1相当于pre替换cur
                count += 1
                cur = cur.next
            # 插入节点
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        # 新建游标
        cur = self.__head
        # 循环遍历
        while cur.next != self.__head:  # 这种条件就限定了循环中不可能出现尾节点情况，也不可能出现只有一个元素的情况
            if cur.elem == item:
                if cur == self.__head:
                    # 头节点
                    # 新建游标,找到尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    # 循环结束，rear指向尾节点
                    # 删除
                    self.__head = cur.next
                    cur.next.prev = None
                    # 尾节点指向头节点
                    rear.next = self.__head
                # else:  # 因循环中不可能出现一个元素的情况故注释掉
                #     # 只有一个元素
                #     self.__head = None
                else:
                    # 中间节点
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                return
            else:
                cur = cur.next
        # 循环结束，cur指向尾节点
        if cur.elem == item:
            if cur.prev is not None:
                cur.prev.next = self.__head
            else:
                self.__head = None

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        # 新建游标
        cur = self.__head
        # 循环遍历
        while cur != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 循环结束，cur指向尾节点
        if cur.elem == item:
            return True
        return False

    def head(self):
        """通过这层包装，继承的子类通过访问此方法来访问私有属性"""
        return self.__head

    def remove_all(self, item):
        """删除链表中所有匹配的节点"""
        if isinstance(item, list):
            # 输入为列表
            if list:
                # 列表不为空
                # 新建游标,找到尾节点
                rear = self.__head  # rear初始值必须在for循环外，使第一次循环后的每次循环前rear都指向尾节点
                for it in item:
                    if self.is_empty():
                        return
                    # 新建游标
                    cur = self.__head  # cur初始值必须在for循环内、第一个while前，每次for循环后cur需要重新指向头节点
                    # 循环遍历
                    while cur.next != self.__head:  # 这种条件就限定了循环中不可能出现尾节点情况，也不可能出现只有一个元素的情况
                        if cur.elem == it:
                            if cur == self.__head:
                                # 头节点
                                while rear.next != self.__head:
                                    rear = rear.next
                                # 循环结束，rear指向尾节点
                                # 删除
                                self.__head = cur.next
                                cur.next.prev = None
                                # 尾节点指向头节点
                                rear.next = self.__head
                                # cur指向下一个节点
                                cur = cur.next
                            else:
                                # 中间节点
                                cur.prev.next = cur.next
                                cur.next.prev = cur.prev
                                # cur指向下一个节点
                                cur = cur.next
                        else:
                            cur = cur.next
                    # 循环结束，cur指向尾节点
                    if cur.elem == it:
                        if cur.prev is not None:
                            cur.prev.next = self.__head
                        else:
                            self.__head = None
        elif isinstance(item, (int, float)):
            # 输入为单个数
            if self.is_empty():
                return
            # 新建游标
            cur = self.__head
            # 新建游标,找到尾节点
            rear = self.__head
            # 循环遍历
            while cur.next != self.__head:  # 这种条件就限定了循环中不可能出现尾节点情况，也不可能出现只有一个元素的情况
                if cur.elem == item:
                    if cur == self.__head:
                        # 头节点
                        while rear.next != self.__head:
                            rear = rear.next
                        # 循环结束，rear指向尾节点
                        # 删除
                        self.__head = cur.next
                        cur.next.prev = None
                        # 尾节点指向头节点
                        rear.next = self.__head
                        # cur指向下一个节点
                        cur = cur.next
                    else:
                        # 中间节点
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev
                        # cur指向下一个节点
                        cur = cur.next
                else:
                    cur = cur.next
            # 循环结束，cur指向尾节点
            if cur.elem == item:
                if cur.prev is not None:
                    cur.prev.next = self.__head
                else:
                    self.__head = None
        else:
            # 输入既不是列表也不是单个数
            return

    def append_list(self, item: list):
        """链表尾部通过列表批量添加元素, 尾插法"""
        if item:
            # 列表不为空
            # 新建游标
            cur = self.__head  # cur的初值应放在循环外面，使第一次循环后的每次循环前cur都指向尾节点
            for it in item:
                # 新建节点
                node = Node(it)
                if self.is_empty():
                    self.__head = node
                    node.next = node
                else:
                    """当第一次找到尾节点后，循环都从尾节点cur开始"""
                    while cur.next != self.__head:
                        cur = cur.next
                    # 循环结束，cur指向尾节点
                    node.next = self.__head
                    node.prev = cur
                    # 插入
                    cur.next = node
                    # 此时cur指向倒数第二位
                    cur = cur.next
                    # 此时cur指向尾节点
        else:
            return

    def add_list(self, item: list):
        """链表头部通过列表批量添加元素，头插法"""
        if item:
            # 列表不为空
            # 新建游标
            cur = self.__head  # cur的初值应放在循环外面，使第一次循环后的每次循环前cur都指向尾节点
            for it in item:
                node = Node(it)
                if self.is_empty():
                    self.__head = node
                    node.next = node
                else:
                    """第一次循环遍历到尾节点之后，循环将从尾节点cur开始，减少了for循环遍历所用时间"""
                    # 循环遍历尾节点
                    while cur.next != self.__head:
                        cur = cur.next
                    # 循环结束，cur指向尾节点
                    node.next = self.__head
                    # 原来的头节点prev指向node
                    node.next.prev = node
                    self.__head = node
                    # 尾节点指向头节点
                    cur.next = self.__head
                    # 此时cur指向尾节点
        else:
            # 列表为空
            return


if __name__ == "__main__":
    # ========= test 1 =========
    # ll = DoubleCycleLinkList()
    # print(ll.is_empty())  # True
    # print(ll.length()) # 0
    #
    # ll.append(1)
    # print(ll.is_empty()) # False
    # print(ll.length())  # 1
    #
    # ll.append(2)
    # ll.add(8)
    # ll.append(3)
    # ll.append(4)
    # ll.append(5)
    # ll.append(6) # 8 1 2 3 4 5 6
    #
    # ll.insert(-1, 9)  # 9 8 1 2 3 4 5 6
    # ll.travel()
    # ll.insert(3, 100)  # 9 8 1 100 2 3 4 5 6
    # ll.travel()
    # ll.insert(10, 200)  # 9 8 1 100 2 3 4 5 6 200
    # ll.travel()
    # ll.remove(100)
    # ll.travel()
    # ll.remove(9)
    # ll.travel()
    # ll.remove(200)
    # ll.travel()  # 8 1 2 3 4 5 6

    # ========= test 2 =========
    ll = DoubleCycleLinkList()
    print(ll.is_empty())  # True
    print(ll.length())  # 0

    ll.append(1)
    print(ll.is_empty())  # False
    print(ll.length())  # 1

    # append/add
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(6)
    ll.append(6)
    ll.append(4)
    ll.append(3)
    ll.append(3)  # 8 1 2 3 4 5 6 6 6 4 3 3

    # insert/remove/remove_all/travel
    ll.insert(-1, 9)  # 9 8 1 2 3 4 5 6 6 6 4 3 3
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3 4 5 6 6 6 4 3 3
    ll.travel()
    ll.insert(20, 200)  # 9 8 1 100 2 3 4 5 6 6 6 4 3 3 200
    ll.travel()
    ll.remove(100)  # 9 8 1 2 3 4 5 6 6 6 4 3 3 200
    ll.travel()
    ll.remove(9)  # 8 1 2 3 4 5 6 6 6 4 3 3 200
    ll.travel()
    ll.remove(200)  # 8 1 2 3 4 5 6 6 6 4 3 3
    ll.travel()
    ll.remove_all(6)  # 8 1 2 3 4 5 4 3 3
    ll.travel()
    ll.remove_all(3)  # 8 1 2 4 5 4
    ll.travel()
    ll.remove_all(4)  # 8 1 2 5
    ll.travel()

    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(3)
    ll.append(6)
    ll.append(6)
    ll.append(4)
    ll.append(3)
    ll.append(3)  # 8 1 2 5 4 5 6 3 6 6 4 3 3
    ll.travel()

    ll.remove_all([6, 3, 4, 5])  # 8, 1, 2
    ll.travel()

    ll.remove_all(8)  # 1, 2
    ll.travel()

    # append_list/add_list
    ll.append_list([3, 4, 5, 6])
    ll.travel()  # 1, 2, 3, 4, 5, 6

    ll.add_list([1, 2, 3])  # 3, 2, 1, 1, 2, 3, 4, 5, 6
    ll.travel()

    # ============= Result ============= #
    #                                    #
    # True                               #
    # 0                                  #
    # False                              #
    # 1                                  #
    # 9 8 1 2 3 4 5 6 6 6 4 3 3          #
    # 9 8 1 100 2 3 4 5 6 6 6 4 3 3      #
    # 9 8 1 100 2 3 4 5 6 6 6 4 3 3 200  #
    # 9 8 1 2 3 4 5 6 6 6 4 3 3 200      #
    # 8 1 2 3 4 5 6 6 6 4 3 3 200        #
    # 8 1 2 3 4 5 6 6 6 4 3 3            #
    # 8 1 2 3 4 5 4 3 3                  #
    # 8 1 2 4 5 4                        #
    # 8 1 2 5                            #
    # 8 1 2 5 4 5 6 3 6 6 4 3 3          #
    # 8 1 2                              #
    # 1 2                                #
    # 1 2 3 4 5 6                        #
    # 3 2 1 1 2 3 4 5 6                  #
    #                                    #
    # ================================== #
