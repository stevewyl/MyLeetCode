def partition(arr, left, right):
    pivot = left # 基准值的index
    index = pivot + 1 # 基准值的插入位置
    i = index # 移动的指针，用于比较当前位置的值与基准值的大小
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index) # 当比基准值小，移到插入指针的左边
            index += 1 # 插入指针右移一位
        i += 1
    swap(arr, pivot, index - 1) # 遍历结束，交换基准值到插入指针的前一位
    return index - 1 # 返回当前基准值的位置

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    # 当left和right位置重合，结束递归调用
    if left < right:
        partition_index = partition(arr, left, right)
        quickSort(arr, left, partition_index - 1) # 对当前基准值左边的子数组进行排序
        quickSort(arr, partition_index + 1, right) # 对右边的子数组进行排序
    return arr