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


class BubbleSort(object):
    """冒泡排序"""

    # def __init__(self):

    def bubble_list(self, alist):
        """列表冒泡排序"""
        n = len(alist)
        for j in range(n - 1):
            # 次循环，排序完成需要进行n-1次循环
            # 计算主循环中交换次数来判断链表是否乱序
            count = 0
            for i in range(n - 1 - j):
                # 主循环，比较相邻连元素大小
                if alist[i] > alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
                    count += 1

            if 0 == count:
                # 第一次遍历后无交换发生，则已排好序
                return

    def bubble_sll(self, sll: SLL.SingleLinkList()):
        """单链表冒泡排序"""
        n = sll.length()
        if sll.is_empty() or sll.length == 1:
            # 若输入链表为空或长度为1，无需排序
            return
        for j in range(n - 1):
            # 次循环，排序完成需要进行n-1次循环
            # 计算主循环中交换次数来判断链表是否乱序
            count = 0
            # 游标
            cur = sll.head()
            # 遍历
            while cur.next is not None:
                # 主循环，比较相邻连元素大小
                if cur.elem > cur.next.elem:
                    cur.elem, cur.next.elem = cur.next.elem, cur.elem
                    count += 1
                cur = cur.next
            # 循环结束，cur指向尾节点
            if count == 0:
                # 第一次for循环后无交换发生，则已排好序
                return

    def bubble_scll(self, scll: SCL.SingleCycleLinkList()):
        """单向循环链表冒泡排序"""
        n = scll.length()
        if scll.is_empty() or scll.length() == 1:
            # 若输入链表为空或长度为1，无需排序
            return
        for j in range(n - 1):
            # 次循环，排序完成需要进行n-1次循环
            # 计算主循环中交换次数来判断链表是否乱序
            count = 0
            cur = scll.head()

            while cur.next != scll.head():
                # 主循环，比较相邻连元素大小
                if cur.elem > cur.next.elem:
                    cur.elem, cur.next.elem = cur.next.elem, cur.elem
                    count += 1
                # cur指向下一个节点
                cur = cur.next
            if count == 0:
                # 第一次for循环后无交换发生，则已排好序
                return

    def bubble_dll(self, dll: DLL.DoubleLinkList()):
        """双链表冒泡排序"""
        # 思路代码几乎和单链表一样
        n = dll.length()
        if dll.is_empty() or dll.length() == 1:
            # 若输入链表为空或长度为1，无需排序
            return
        for j in range(n - 1):
            # 次循环，排序完成需要进行n-1次循环
            # 计算主循环中交换次数来判断链表是否乱序
            count = 0
            cur = dll.head()
            while cur.next is not None:
                if cur.elem > cur.next.elem:
                    cur.elem, cur.next.elem = cur.next.elem, cur.elem
                    count += 1
                    # cur指向下一个节点
                cur = cur.next
            # 循环结束，cur指向尾节点
            if count == 0:
                # 第一次for循环后无交换发生，则已排好序
                return

    def bubble_dcll(self, dcll: DCL.DoubleCycleLinkList()):
        """双向循环链表冒泡排序"""
        # 思路代码几乎和双链表循环一样
        n = dcll.length()
        if dcll.is_empty() or dcll.length() == 1:
            # 若输入链表为空或长度为1，无需排序
            return
        for j in range(n - 1):
            # 次循环，排序完成需要进行n-1次循环
            # 计算主循环中交换次数来判断链表是否乱序
            count = 0
            cur = dcll.head()

            while cur.next != dcll.head():
                # 主循环，比较相邻连元素大小
                if cur.elem > cur.next.elem:
                    cur.elem, cur.next.elem = cur.next.elem, cur.elem
                    count += 1
                # cur指向下一个节点
                cur = cur.next
            if count == 0:
                # 第一次for循环后无交换发生，则已排好序
                return


if __name__ == "__main__":
    # ================== test ================== #
    bubble = BubbleSort()

    # 列表冒泡排序测试
    print("List Bubble:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble.bubble_list(li)
    print(li)  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print()

    # 单链表冒泡排序测试
    print("SingleLinkList Bubble:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sll = SLL.SingleLinkList()
    sll.append_list(li)
    bubble.bubble_sll(sll)
    sll.travel()  # 17 20 26 31 44 54 55 77 93
    print()

    # 单向循环链表冒泡排序测试
    print("SingleCycleLinkList Bubble:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    scll = SCL.SingleCycleLinkList()
    scll.append_list(li)
    bubble.bubble_scll(scll)
    scll.travel()  # 17 20 26 31 44 54 55 77 93
    print()

    # 双向循环链表冒泡排序测试
    print("DoubleCycleLinkList Bubble:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    dcll = DCL.DoubleCycleLinkList()
    dcll.append_list(li)
    bubble.bubble_dcll(dcll)
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
    # ====================================== #
