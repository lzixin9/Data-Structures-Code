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

class InsertSort(object):
    """插入排序"""

    def insert_list(self, alist: list):
        """列表插入排序"""
        n = len(alist)
        # 从右边的无序序列中取出多少个元素执行这样的过程
        for j in range(1, n):  # j: 1 ~ n-1
            # i 代表内层循环起始值
            i = j
            # 执行从右边的无序序列中取出第一个元素，即i位置的元素，将其插入到前面的正确位置中
            while i > 0:
                if alist[i] < alist[i - 1]:
                    alist[i], alist[i - 1] = alist[i - 1], alist[i]
                    i -= 1
                else:
                    break

    # def insert_sll(self, sll: SLL.SingleLinkList()):
    #     """单链表插入排序"""
    #     n = sll.length()
    #     if n == 0 or n == 1:
    #         # 列表为0或1，无需排序
    #         return
    #     pre = sll.head()
    #     for j in range(n - 1):
    #         cur = pre.next
    #         # while pre != cur:

    def insert_dll(self, dll: DLL.DoubleLinkList()):
        """双链表插入排序"""
        n = dll.length()
        if n == 0 or n == 1:
            # 列表为0或1，无需排序
            return
        # cur指向乱序节点，从前往后走
        cur = dll.head().next
        while cur is not None:
            # rem记录cur走到的最远位置
            rem = cur
            while cur.prev is not None:  # for i in range(n-1):  # 排序需要n-1次循环 两种用法皆可
                if cur.prev.elem > cur.elem:
                    cur.prev.elem, cur.elem = cur.elem, cur.prev.elem
                cur = cur.prev
            # 循环结束，cur指向None,rem指向cur走到的最远位置节点
            # 移动指针
            cur = rem.next

    def insert_dcll(self, dcll: DCL.DoubleCycleLinkList()):
        """双向循环链表插入排序"""
        n = dcll.length()
        if n == 0 or n == 1:
            # 列表为0或1，无需排序
            return
        # cur指向乱序节点，从前往后走
        cur = dcll.head().next
        while cur.next != dcll.head():
            # rem记录cur走到的最远位置
            rem = cur
            while cur.next != dcll.head():  # for i in range(n-1):  # 排序需要n-1次循环 两种用法皆可
                # cur往前移动到第二个节点
                if cur.prev.elem > cur.elem:
                    cur.prev.elem, cur.elem = cur.elem, cur.prev.elem
                cur = cur.prev
            # 循环结束，cur指向头节点,rem指向cur走到的最远位置节点
            if cur.prev.elem > cur.elem:
                cur.prev.elem, cur.elem = cur.elem, cur.prev.elem
            # 移动指针
            cur = rem.next


if __name__ == "__main__":
    # ================== test ================== #
    insert = InsertSort()

    # 列表选择排序测试
    print("List Insert:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert.insert_list(li)
    print(li)  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print()

    # # 单链表选择排序测试
    # print("SingleLinkList Insert:")
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # sll = SLL.SingleLinkList()
    # sll.append_list(li)
    # select.select_sll(sll)
    # sll.travel()  # 17 20 26 31 44 54 55 77 93
    # print()
    #
    # # 单向循环链表选择排序测试
    # print("SingleCycleLinkList Insert:")
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # scll = SCL.SingleCycleLinkList()
    # scll.append_list(li)
    # select.select_scll(scll)
    # scll.travel()  # 17 20 26 31 44 54 55 77 93
    # print()
    #
    # 双链表选择排序测试
    print("DoubleLinkList Insert:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    dll = DLL.DoubleLinkList()
    dll.append_list(li)
    insert.insert_dll(dll)
    dll.travel()  # 17 20 26 31 44 54 55 77 93
    print()

    # 双向循环链表冒泡排序测试
    print("DoubleCycleLinkList Insert:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    dcll = DCL.DoubleCycleLinkList()
    dcll.append_list(li)
    insert.insert_dcll(dcll)
    dcll.travel()  # 17 20 26 31 44 54 55 77 93
    print()

    # =============== Result =============== #
    # List Insert:                           #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # [17, 20, 26, 31, 44, 54, 55, 77, 93]   #
    #                                        #
    # SingleLinkList Insert:                 #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # 17 20 26 31 44 54 55 77 93             #
    #                                        #
    # SingleCycleLinkList Insert:            #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # 17 20 26 31 44 54 55 77 93             #
    #                                        #
    # DoubleLinkList Insert:                 #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # 17 20 26 31 44 54 55 77 93             #
    #                                        #
    # DoubleCycleLinkList Insert:            #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # 17 20 26 31 44 54 55 77 93             #
    #                                        #
    # ====================================== #
