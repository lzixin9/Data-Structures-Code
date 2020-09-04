# coding:utf-8


class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # 游标 cusor
        cur = self.__head
        # 计数
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print()

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:  # 记住这里是cur.next != None而不是cur != None
                cur = cur.next
            cur.next = node

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param  pos 从0开始
        """
        pre = self.__head  # 注意这里用的是pre！所以while判断语句count是与pos-1比较！若是cur则应该是与pos比较
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        """删除节点"""
        pre = None
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def head(self):  # 通过这层包装，继承的子类通过访问此方法来访问私有属性
        """Through this layer of packaging,
        inherited subclasses access private properties by accessing this method"""
        return self.__head

    def remove_all(self, item):
        """
        删除所有与输入匹配的节点  Delete all nodes that match the input
        :param item: list or single number
        :return:
        """
        if isinstance(item, list):
            # 输入为列表
            if item:
                # 列表不为空
                for it in item:
                    pre = None
                    cur = self.__head
                    # 遍历
                    while cur is not None:
                        if cur.elem == it:
                            # 移除的元素在头部
                            if cur == self.__head:
                                self.__head = cur.next
                                cur = cur.next
                            else:
                                pre.next = cur.next
                                cur = cur.next
                        else:
                            pre = cur
                            cur = cur.next
            else:
                # 列表为空
                return
        elif isinstance(item, (int, float)):
            # 输入为单个数字
            # 游标
            pre = None
            cur = self.__head
            while cur is not None:
                if cur.elem == item:
                    if cur == self.__head:
                        self.__head = cur.next
                        cur = cur.next
                    else:
                        pre.next = cur.next
                        cur = cur.next
                else:
                    pre = cur
                    cur = cur.next
        else:
            # 输入既不是列表也不是单个数字
            return

    def append_list(self, item: list):
        """链表尾部通过列表批量添加元素, 尾插法"""
        if list:
            # 游标
            cur = self.__head  # cur的初值应放在循环外面，使第一次循环后的每次循环前cur都指向尾节点
            for it in item:
                # 创建节点
                node = Node(it)
                if self.is_empty():
                    # 链表为空
                    self.__head = node
                else:
                    # 链表不为空
                    # 遍历到尾节点
                    """第一次循环遍历到尾节点之后，循环将从尾节点cur开始，减少了for循环遍历所用时间"""
                    while cur.next is not None:  # 记住这里是cur.next != None而不是cur != None
                        cur = cur.next
                    # 循环结束，cur指向尾节点
                    cur.next = node
                    # 此时cur指向倒数第二个节点
                    cur = cur.next
                    # 此时cur指向尾节点
        else:
            return

    def add_list(self, item: list):
        """链表头部通过列表批量添加元素，头插法"""
        if list:
            for it in item:
                node = Node(it)
                node.next = self.__head
                self.__head = node
            else:
                return


if __name__ == "__main__":
    # ========= test 1 =========
    # ll = SingleLinkList()
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
    ll = SingleLinkList()
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
