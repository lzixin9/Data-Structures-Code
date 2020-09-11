# coding:utf-8


def binary_search(alist, item):
    """二分查找,递归"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)  # 注意这里列表索引是从mid + 1开始
    return False


def binary_search_2(alist, item):
    """二分查找， 非递归"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print("Binary Search(Recursion):")
    print("Judge 55 in list:", binary_search(li, 55))
    print("Judge 100 in list:", binary_search(li, 100))
    print("Binary Search:")
    print("Judge 55 in list:", binary_search_2(li, 55))
    print("Judge 100 in list:", binary_search_2(li, 100))

    # ========= Result ========= #
    # Binary Search(Recursion):  #
    # Judge 55 in list: True     #
    # Judge 100 in list: False   #
    # Binary Search:             #
    # Judge 55 in list: True     #
    # Judge 100 in list: False   #
    # ========================== #
