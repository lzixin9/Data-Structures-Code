# coding:utf-8


class Node(object):
    """结点"""

    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # 定义游标
        cur = self.__head
        # 计数
        count = 0
        # 遍历
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        # 定义游标
        cur = self.__head
        # 遍历
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print()

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        if node.next:
            # 判断是否为尾节点
            node.next.prev = node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        # 创建新增节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            # 定义一个游标
            cur = self.__head
            # 遍历
            while cur.next is not None:  # 记住这里是cur.next != None而不是cur != None
                cur = cur.next
            # 尾插
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """
        指定位置添加元素
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
        # 定义游标
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break  # break不要忘记，这是仅删除遍历到的第一个元素
            else:
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        # 定义游标
        cur = self.__head
        # 遍历
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
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
                for it in item:
                    # 定义游标
                    cur = self.__head
                    # 遍历
                    while cur is not None:
                        if cur.elem == it:
                            # 找到删除元素
                            if cur == self.__head:
                                # 删除元素在头部
                                self.__head = cur.next

                                if cur.next:
                                    # 若节点数不止一个，cur后一个节点指向None
                                    cur.next.prev = None
                                cur = cur.next
                                # 此时cur指向尾节点
                            else:
                                # 删除元素不在头部
                                cur.prev.next = cur.next
                                if cur.next:
                                    # 若节点数不止一个，cur后一个节点指向None
                                    cur.next.prev = cur.prev
                                # cur指向下一个节点
                                cur = cur.next
                                # 此时cur指向尾节点
                        else:
                            cur = cur.next
        elif isinstance(item, (int, float)):
            # 输入为单个数字
            # 定义游标
            cur = self.__head
            # 遍历
            while cur is not None:
                if cur.elem == item:
                    # 找到删除元素
                    if cur == self.__head:
                        # 删除元素在头部
                        self.__head = cur.next
                        # cur指向下一个节点
                        cur = cur.next
                        if cur.next:
                            # 若节点数不止一个，cur后一个节点指向None
                            cur.next.prev = None
                    else:
                        # 删除元素不在头部
                        cur.prev.next = cur.next
                        if cur.next:
                            # 若节点数不止一个，cur后一个节点指向None
                            cur.next.prev = cur.prev
                        # cur指向下一个节点，这个位置只能放在if下面
                        cur = cur.next

                else:
                    cur = cur.next
        else:
            # 输入既不是列表也不是单个数字
            return

    def append_list(self, item: list):
        """链表尾部通过列表批量添加元素, 尾插法"""
        if item:
            # 列表不为空
            # 定义一个游标
            cur = self.__head  # cur的初值应放在循环外面，使第一次循环后的每次循环前cur都指向尾节点
            for it in item:
                # 创建新增节点
                node = Node(it)
                if self.is_empty():
                    self.__head = node
                    cur = node
                else:
                    # 遍历
                    """第一次循环遍历到尾节点之后，循环将从尾节点cur开始，减少了for循环遍历所用时间"""
                    while cur.next is not None:  # 记住这里是cur.next != None而不是cur != None
                        cur = cur.next
                    # 循环结束，cur指向尾节点
                    # 尾插
                    # 这里cur变成指向倒数第二个节点
                    cur.next = node
                    node.prev = cur
                    # 此时cur指向倒数第二个节点
                    cur = cur.next
                    # 此时cur指向尾节点
        else:
            # 列表为空
            return

    def add_list(self, item: list):
        """链表头部通过列表批量添加元素，头插法"""
        if item:
            # 列表不为空
            for it in item:
                node = Node(it)
                node.next = self.__head
                self.__head = node
                if node.next:
                    # 判断是否为尾节点
                    node.next.prev = node
        else:
            # 列表为空
            return


if __name__ == "__main__":
    # ========= test 1 =========
    # ll = DoubleLinkList()
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
    ll = DoubleLinkList()
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