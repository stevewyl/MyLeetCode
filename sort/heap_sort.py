def down_adjust(parent_index, length, array=[]):
    # temp保存父节点的值，用于最后的赋值
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        # 有右孩子且右孩子值大于左孩子，定位到右孩子
        if child_index + 1 < length and array[child_index + 1] > array[child_index]:
            child_index += 1
        # 父节点值大于任何一个孩子的值，直接跳出
        if temp >= array[child_index]:
            break
        # 单向赋值
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = child_index * 2 + 1
    array[parent_index] = temp

def heap_sort(array=[]):
    # 无序数组 -> 最大堆
    for i in range((len(array) - 2) // 2, -1, -1):
        down_adjust(i, len(array), array)
    # 循环交换尾部元素到堆顶，并调整堆形成新的堆顶
    for i in range(len(array) - 1, 0, -1):
        # 最后一个元素和第一个元素交换
        temp = array[i]
        array[i] = array[0]
        array[0] = temp
        # 下沉调整最大堆
        down_adjust(0, i, array)