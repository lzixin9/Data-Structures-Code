# coding:utf-8


def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    # 若列表为空或长度为1，无需排序
    if n <= 1:
        return alist
    mid = n // 2

    # =================================================== 递归 =========================================================
    # 代码run到这，会先进入第一个递归代码行，直到alist只有一个元素，在上述的if语句后，返回1个元素的列表存在上一个递归函数的left_li中
    # 上一个递归函数得到left_li值后，进入下一个递归函数同样得到right_li的值，通过下述while循环排序之后得到返回值，得到上一个left_li
    # 和right_li的值，以此类推，直到得到第一层函数的返回值
    # left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])
    # ==================================================================================================================

    # 将两个有序的子序列合并为一个新的整体
    left_pointer, right_pointer = 0, 0
    result = []
    # 从left_li和right_li中通过比较挑选元素，若其中一个列表走到末尾则直接跳出循环，将剩下的列表元素直接合并到result列表即可
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == "__main__":
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    li = [1, 2, 3, 4, 5, 6, 7, 8]
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_li = merge_sort(li)
    print(li)  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(sorted_li)  # [17, 20, 26, 31, 44, 54, 55, 77, 93]

    # ============== Result ============== #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20] #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20] #
    # [17, 20, 26, 31, 44, 54, 55, 77, 93] #
    # ==================================== #
