# coding:utf-8


def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # high 左移
        while low < high and alist[high] >= mid_value:  # 两个while循环中只能有一个等号
            high -= 1
        # 因为alist[low]已保存在mid_value中，相当于与中值互换位置
        alist[low] = alist[high]
        # low 右移
        while low < high and alist[low] < mid_value:
            low += 1
        # 因为alist[high]已保存在mid_value中，相当于与中值互换位置
        alist[high] = alist[low]
    # 从循环退出时，low=high，即找到中值的位置
    alist[low] = mid_value
    # 此时以中值为界分为左右两个无序部分，左边序列的值都比中值小，右边序列的值都比中值大

    # 递归
    # 对low左边的列表执行快速排序
    quick_sort(alist, first, low - 1)
    # 对low右边的列表排序
    quick_sort(alist, low + 1, last)


if __name__ == "__main__":
    # ================ test ================ #
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
    # =============== Result =============== #
    # [54, 26, 93, 17, 77, 31, 44, 55, 20]   #
    # [17, 20, 26, 31, 44, 54, 55, 77, 93]   #
    # ====================================== #
