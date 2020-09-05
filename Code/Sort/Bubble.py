# coding:utf-8

import Data_Structure.LinkList.SingleLinkList as SLL


class BubbleSort(object):
    """冒泡排序"""

    # def __init__(self):

    def bubble_list(self, alist):
        """列表冒泡排序"""
        n = len(alist)
        for j in range(n - 1):
            # 次循环，排序完成需要进行n-1次遍历
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
        for j in range(n - 1):
            # 次循环，排序完成需要进行n-1次遍历
            # 计算主循环中交换次数来判断链表是否乱序
            count = 0
            # 游标
            cur = sll.head()
            # 遍历
            if sll.is_empty() or sll.length == 1:
                # 若输入链表为空或长度为1，无需排序
                return
            else:
                while cur.next is not None:
                    # 主循环，比较相邻连元素大小
                    if cur.elem > cur.next.elem:
                        cur.elem, cur.next.elem = cur.next.elem, cur.elem
                    cur = cur.next
                # 循环结束，cur指向尾节点
                if count == 0:
                    # 第一次遍历后无交换发生，则已排好序
                    return


if __name__ == "__main__":
    # ================== test ================== #
    bubble = BubbleSort()

    # 列表冒泡排序测试
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("List Bubble:")
    print(li)  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print()

    # 单链表冒泡排序测试
    print("SingleLinkList Bubble:")
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sll = SLL.SingleLinkList()
    sll.append_list(li)
    bubble.bubble_sll(sll)
    sll.travel() # 17 20 26 31 44 54 55 77 93

    # =============== Result =============== #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # List Bubble:                           #
    # [17, 20, 26, 31, 44, 54, 55, 77, 93]   #
    # SingleLinkList Bubble:                 #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # 26 54 17 77 31 44 55 20 93             #
    #                                        #
    # ====================================== #
