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

class SelectSort(object):
    """选择排序"""

    def select_list(self, alist: list):
        """列表选择排序"""
        n = len(alist)
        if n == 0 or n == 1:
            # 列表为0或1，无需排序
            return
        for j in range(n - 1):  # j: 0 ~ n-2
            # 次循环，排序完成需要进行n-1次循环
            min_index = j
            # 获得相对最小值的索引需要和剩余未排序元素比较，故循环范围取到n-1
            for i in range(j + 1, n):  # i: j + 1 ~ n-1
                # 主循环，比较元素大小和交换操作
                if alist[min_index] > alist[i]:
                    min_index = i
            alist[j], alist[min_index] = alist[min_index], alist[j]

    def select_sll(self, sll: SLL.SingleLinkList()):
        """单链表选择排序"""
        n = sll.length()
        if n == 0 or n == 1:
            # 链表长度为0或1，无需排序
            return
        # cmp存储最小元素节点
        cmp = sll.head()
        while cmp.next is not None:
            # 次循环，排序完成需要进行n-1次循环
            cur = cmp.next
            # 因需对最后节点元素进行操作，所以循环条件是cur而不是cur.next
            while cur is not None:
                if cmp.elem > cur.elem:
                    cmp.elem, cur.elem = cur.elem, cmp.elem
                cur = cur.next
            # 循环结束，cur指向None

            # cmp指向下一个节点
            cmp = cmp.next

    def select_scll(self, scll: SCL.SingleCycleLinkList()):
        """单向循环链表选择排序"""
        n = scll.length()
        if n == 0 or n == 1:
            # 链表长度为0或1，无需排序
            return
        # cmp存储最小元素节点
        cmp = scll.head()
        while cmp.next != scll.head():
            # 次循环，排序完成需要进行n-1次循环
            cur = cmp.next
            while cur.next != scll.head():
                if cmp.elem > cur.elem:
                    cmp.elem, cur.elem = cur.elem, cmp.elem
                cur = cur.next
            # 循环结束，cur指向尾节点
            # 对最后一个元素进行比较
            if cmp.elem > cur.elem:
                cmp.elem, cur.elem = cur.elem, cmp.elem
            # cmp指向下一个节点
            cmp = cmp.next

    def select_dll(self, dll: DLL.DoubleLinkList()):
        """双链表选择排序"""
        # 代码和单链表几乎一样，因为不用考虑prev，将其看作单链表
        n = dll.length()
        if n == 0 or n == 1:
            # 链表长度为0或1，无需排序
            return
        # cmp存储最小元素节点
        cmp = dll.head()
        while cmp.next is not None:
            # 次循环，排序完成需要进行n-1次循环
            cur = cmp.next
            # 因需对最后节点元素进行操作，所以循环条件是cur而不是cur.next
            while cur is not None:
                if cmp.elem > cur.elem:
                    cmp.elem, cur.elem = cur.elem, cmp.elem
                cur = cur.next
            # 循环结束，cur指向None

            # cmp指向下一个节点
            cmp = cmp.next

    def select_dcll(self, dcll: DCL.DoubleCycleLinkList()):
        """双向循环链表选择排序"""
        # 代码和单循环链表几乎一样，因为不用考虑尾节点指向头部，将其看作单循环链表
        n = dcll.length()
        if n == 0 or n == 1:
            # 链表长度为0或1，无需排序
            return
        # cmp存储最小元素节点
        cmp = dcll.head()
        while cmp.next != dcll.head():
            # 次循环，排序完成需要进行n-1次循环
            cur = cmp.next
            while cur.next != dcll.head():
                if cmp.elem > cur.elem:
                    cmp.elem, cur.elem = cur.elem, cmp.elem
                cur = cur.next
            # 循环结束，cur指向尾节点
            # 对最后一个元素进行比较
            if cmp.elem > cur.elem:
                cmp.elem, cur.elem = cur.elem, cmp.elem
            # cmp指向下一个节点
            cmp = cmp.next


if __name__ == "__main__":
    # ================== test ================== #
    select = SelectSort()

    # 列表选择排序测试
    print("List Select:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    select.select_list(li)
    print(li)  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print()

    # 单链表选择排序测试
    print("SingleLinkList Select:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sll = SLL.SingleLinkList()
    sll.append_list(li)
    select.select_sll(sll)
    sll.travel()  # 17 20 26 31 44 54 55 77 93
    print()

    # 单向循环链表选择排序测试
    print("SingleCycleLinkList Select:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    scll = SCL.SingleCycleLinkList()
    scll.append_list(li)
    select.select_scll(scll)
    scll.travel()  # 17 20 26 31 44 54 55 77 93
    print()

    # 双链表选择排序测试
    print("DoubleLinkList Select:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    dll = DLL.DoubleLinkList()
    dll.append_list(li)
    select.select_dll(dll)
    dll.travel()  # 17 20 26 31 44 54 55 77 93
    print()

    # 双向循环链表冒泡排序测试
    print("DoubleCycleLinkList Select:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    dcll = DCL.DoubleCycleLinkList()
    dcll.append_list(li)
    select.select_dcll(dcll)
    dcll.travel()  # 17 20 26 31 44 54 55 77 93
    print()

    # =============== Result =============== #
    # List Bubble:                           #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # [17, 20, 26, 31, 44, 54, 55, 77, 93]   #
    #                                        #
    # SingleLinkList Bubble:                 #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # 17 20 26 31 44 54 55 77 93             #
    #                                        #
    # SingleCycleLinkList Bubble:            #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # 17 20 26 31 44 54 55 77 93             #
    #                                        #
    # DoubleLinkList Bubble:                 #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # 17 20 26 31 44 54 55 77 93             #
    #                                        #
    # DoubleCycleLinkList Bubble:            #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # 17 20 26 31 44 54 55 77 93             #
    #                                        #
    # ====================================== #


