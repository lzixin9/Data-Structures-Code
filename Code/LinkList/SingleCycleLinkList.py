class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None


class SingleCycleLinkList(object):
    def __init__(self, node=None):
        self.__head = node
        # 增加尾指向头
        if node:
            node.next = self.__head

    def is_empty(self):
        return self.__head is None

    def length(self):
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
                else:
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


if __name__ == "__main__":
    ll = SingleCycleLinkList()
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
    ll.insert(-1, 9)  # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
