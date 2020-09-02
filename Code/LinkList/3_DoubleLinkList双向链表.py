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


if __name__ == "__main__":
    ll = DoubleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 2 3 4 5 6
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3 4 5 6
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 2 3 4 5 6 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()  # 8 1 2 3 4 5 6
