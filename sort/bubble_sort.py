def bubble_sort_v1(array=[]):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


def bubble_sort_v2(array=[]):
    for i in range(len(array) - 1):
        # 有序标记，每一轮的初始为True
        is_sorted = True
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                # 有元素交换，则不是有序的，标记为False
                is_sorted = False
            if is_sorted:
                break


def bubble_sort_v3(array=[]):
    # 记录最后一次交换的位置
    last_exchange_index = 0
    # 无序数列的边界，每次比较只需要到这里
    sort_border = len(array) - 1
    for i in range(len(array) - 1):
        # 有序标记，每一轮的初始为True
        is_sorted = True
        for j in range(sort_border):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                # 有元素交换，则不是有序的，标记为False
                is_sorted = False
                # 把无序数列的边界更新为最后一次交换元素的位置
                last_exchange_index = j
            sort_border = last_exchange_index
            if is_sorted:
                break


def cock_tail_sort(array=[]):
    for i in range(len(array) // 2):
        is_sorted = True
        # 奇数轮，从左向右比较和交换
        for j in range(i, len(array)-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                is_sorted = False
        if is_sorted:
            break
        # 偶数轮前，重新标记为True
        is_sorted = True
        # 偶数轮，从右向左进行比较
        for j in range(len(array)-1-i, i, -1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                is_sorted = False
        if is_sorted:
            break


if __name__ == '__main__':
    from copy import deepcopy

    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    bubble_sort_v1(deepcopy(my_array)) # 13.4us
    bubble_sort_v2(deepcopy(my_array)) # 8.05us
    bubble_sort_v3(deepcopy(my_array)) # 6.79us
    cock_tail_sort(deepcopy(my_array)) # 12.3us
    my_array = [2, 3, 4, 5, 6, 7, 1, 8]
    bubble_sort_v2(deepcopy(my_array)) # 5.37us
    cock_tail_sort(deepcopy(my_array)) # 5.56us