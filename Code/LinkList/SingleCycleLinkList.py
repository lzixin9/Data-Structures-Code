# coding:utf-8


class Node(object):
    """节点"""

    def __init__(self, item):
        self.elem = item
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""

    def __init__(self, node=None):
        self.__head = node
        # 增加尾指向头
        if node:
            node.next = self.__head

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # 定义游标
        cur = self.__head
        # cur为None，cur.next不存在情况,即链表为空
        if self.is_empty():
            return 0
        # 计数
        count = 1  # 因为尾节点指向head，改成1
        while cur.next != self.__head:  # 因为尾节点指向head，cur改成cur.next
            count += 1
            cur = cur.next
        # 循环结束，游标指向尾节点
        return count

    def travel(self):
        """遍历整个链表"""
        # cur为None，cur.next不存在情况,即链表为空
        if self.is_empty():
            return  # 跳出
        # 定义游标
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 循环结束，游标指向尾节点
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素，头插法"""
        # 新建节点
        node = Node(item)
        # cur为None，cur.next不存在情况,即链表为空
        if self.is_empty():
            self.__head = node
            # 尾节点指向头节点
            node.next = node
        # 创建游标
        else:
            cur = self.__head
            # 遍历到尾节点
            while cur.next != self.__head:
                cur = cur.next
            # 循环结束，游标指向尾节点
            # 头节点插入新节点
            node.next = self.__head
            self.__head = node
            # 尾节点指向头节点
            cur.next = node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        # 新建节点
        node = Node(item)
        # cur为None，cur.next不存在情况,即链表为空
        if self.is_empty():
            self.__head = node
            # 尾节点指向头节点
            node.next = node
        else:
            # 创建游标
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 循环结束，游标指向尾节点
            # 新增尾节点指向头节点
            node.next = self.__head
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
            # 创建游标
            pre = self.__head
            # 计数
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            # 循环结束，游标pre指向插入节点前一个节点
            # 新建节点
            node = Node(item)
            # 插入
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        # 创建游标
        cur = self.__head
        pre = None
        if self.is_empty():
            return
        # 循环遍历
        while cur.next != self.__head:
            if cur.elem == item:
                # 头节点
                if cur == self.__head:
                    # 创建游标
                    rear = self.__head
                    # self.__head = cur.next
                    # 找尾节点
                    while rear.next != self.__head:
                        rear = rear.next
                    # 循环结束，游标指向尾节点
                    # 删除并重新指向
                    self.__head = cur.next
                    rear.next = cur.next
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 游标指向尾节点
        # 移除尾节点
        if cur.elem == item:
            # 链表中只有一个元素
            if self.length() == 1:
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        # 创建游标
        cur = self.__head
        # 循环遍历
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 结束循环，游标指向尾节点
        if cur.elem == item:
            return True
        return False

    def head(self):  # 通过这层包装，继承的子类通过访问此方法来访问私有属性
        return self.__head

    def remove_all(self, item):
        """
        删除所有与输入匹配的节点
        """
        if isinstance(item, list):
            # 输入为列表
            if item:
                # 列表不为空
                # 创建游标rear
                rear = self.__head  # rear初始值必须在for循环外，使第一次循环后的每次循环前rear都指向尾节点
                for it in item:
                    # 创建游标cur
                    cur = self.__head  # cur初始值必须在for循环内、第一个while前，每次for循环后cur需要重新指向头节点
                    pre = None
                    if self.is_empty():
                        return
                    # 循环遍历
                    while cur.next != self.__head:
                        if cur.elem == it:
                            # 头节点
                            if cur == self.__head:
                                # self.__head = cur.next
                                # 找尾节点
                                """第一次循环遍历到尾节点之后，循环将从尾节点rear开始，减少了for循环遍历所用时间"""
                                while rear.next != self.__head:
                                    rear = rear.next
                                # 循环结束，游标指向尾节点
                                # 删除并重新指向
                                self.__head = cur.next
                                rear.next = cur.next
                                # 游标指向后一个元素
                                cur = cur.next
                                # 此时rear指向尾节点
                            else:
                                # 中间节点
                                pre.next = cur.next
                                # 游标指向后一个元素
                                cur = cur.next
                        else:
                            pre = cur
                            cur = cur.next
                    # 游标指向尾节点
                    # 移除尾节点
                    if cur.elem == it:
                        # 链表中只有一个元素
                        if self.length() == 1:
                            self.__head = None
                        else:
                            pre.next = cur.next
                else:
                    # 列表为空
                    return
        elif isinstance(item, (int, float)):
            # 输入为单个数字
            # 创建游标
            cur = self.__head
            pre = None
            if self.is_empty():
                return
            # 循环遍历
            while cur.next != self.__head:
                if cur.elem == item:
                    # 移除头节点
                    if cur == self.__head:
                        # 移除中间点
                        # 创建游标
                        rear = self.__head
                        # self.__head = cur.next
                        # 找尾节点
                        while rear.next != self.__head:
                            rear = rear.next
                        # 循环结束，游标指向尾节点
                        # 删除并重新指向
                        self.__head = cur.next
                        rear.next = cur.next
                        cur = cur.next
                    else:
                        pre.next = cur.next
                        cur = cur.next
                else:
                    pre = cur
                    cur = cur.next
            # 游标指向尾节点
            # 移除尾节点
            if cur.elem == item:
                # 链表中只有一个元素
                if self.length() == 1:
                    self.__head = None
                else:
                    pre.next = cur.next
        else:
            # 输入既不是列表也不是数字
            return

    def append_list(self, item: list):
        """链表尾部通过列表批量添加元素, 尾插法"""
        if list:
            # 创建游标
            cur = self.__head  # cur的初值应放在循环外面，使第一次循环后的每次循环前cur都指向尾节点
            for it in item:
                # 新建节点
                node = Node(it)
                # cur为None，cur.next不存在情况,即链表为空
                if self.is_empty():
                    self.__head = node
                    # 尾节点指向头节点
                    node.next = node
                    cur = node
                    # 此时cur指向尾节点
                else:
                    """第一次循环遍历到尾节点后，循环将从尾节点cur开始，减少for循环遍历所用时间"""
                    while cur.next != self.__head:
                        cur = cur.next
                    # 循环结束，游标指向尾节点
                    # 新增尾节点指向头节点
                    node.next = self.__head
                    cur.next = node
                    # 此时cur指向倒数第二节点，需后移一位
                    cur = cur.next
                    # 此时cur指向尾节点
        else:
            return

    def add_list(self, item: list):
        """链表头部通过列表批量添加元素，头插法"""
        if item:
            # 列表非空
            for it in item:
                # 新建节点
                node = Node(it)
                cur = self.__head
                # cur为None，cur.next不存在情况,即链表为空
                if self.is_empty():
                    self.__head = node
                    # 尾节点指向头节点
                    node.next = node
                # 创建游标
                else:
                    """第一次循环遍历到尾节点之后，循环将从尾节点cur开始，减少了for循环遍历所用时间"""
                    # 遍历到尾节点
                    while cur.next != self.__head:
                        cur = cur.next
                    # 循环结束，游标指向尾节点
                    # 头节点插入新节点
                    node.next = self.__head
                    self.__head = node
                    # 尾节点指向头节点
                    cur.next = node
                    # 此时cur指向尾节点
        else:
            # 列表为空
            return


if __name__ == "__main__":
    # ========= test 1 =========
    # ll = SingleCycleLinkList()
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
    ll = SingleCycleLinkList()
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
