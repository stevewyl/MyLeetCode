# 双指针
def partition_v1(arr, start, end):
    pivot = start
    left = start
    right = end
    while left != right:
        while left < right and arr[right] > pivot:
            right -= 1
        while left < right and arr[left] <= pivot:
            left += 1
        if left < right:
            swap(arr, left, right)
    swap(arr, pivot, left)
    return left

# 单指针
def partition_v2(arr, start, end):
    pivot = start # 基准值的index
    mark = start # 基准值的插入位置
    for i in range(start + 1, end + 1):
        if arr[i] < arr[pivot]:
            mark += 1 # 插入指针右移一位
            swap(arr, i, mark) # 当比基准值小，移到插入指针的左边
    swap(arr, pivot, mark) # 遍历结束，交换基准值到插入指针
    return mark # 返回当前基准值的位置

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort_v1(arr, left=None, right=None, partition_v=1):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    # 当left和right位置重合，结束递归调用
    if left < right:
        if partition_v == 1:
            partition_index = partition_v1(arr, left, right)
        else:
            partition_index = partition_v2(arr, left, right)
        quickSort_v1(arr, left, partition_index - 1, partition_v) # 对当前基准值左边的子数组进行排序
        quickSort_v1(arr, partition_index + 1, right, partition_v) # 对右边的子数组进行排序
    return arr

# 非递归实现
def quickSort_v2(arr, left, right):
    pass

if __name__ == "__main__":
    from copy import deepcopy

    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    print(quickSort_v1(deepcopy(my_array), partition_v=1))
    print(quickSort_v1(deepcopy(my_array), partition_v=2))