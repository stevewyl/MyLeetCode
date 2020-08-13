import random
import time

def print_run_time(func):
    def wrapper(*args, **kw):
        local_time = time.time()
        func(*args, **kw)
        print('current Function [%s] run time is %.4f' % (func.__name__ , (time.time() - local_time) * 1000))
    return wrapper

# 方法一：排序
# O(nlogn)
@print_run_time
def solution1(arr, k):
    return sorted(arr)[-k]

# 方法二：插入
# O(nk)，当k比较大的时候，不如方法一
@print_run_time
def solution2(arr, k):
    sorted_topk_arr = sorted(arr[:k])
    for i in range(k, len(arr) - 1):
        if arr[i] > sorted_topk_arr[0]:
            sorted_topk_arr = sorted([arr[i]] + sorted_topk_arr[1:])
    return sorted_topk_arr[0]

# 方法三：小顶堆
# 最坏O((n-k)logk+k)
# 最好O(nlogk)，当k远小于n
# 空间复杂度：由于是原地交换元素，没有额外的空间开销 -> O(1)
@print_run_time
def solution3(arr, k):
    # O(k)
    def build_heap(arr, length):
        last_father = int((length - 2) / 2) # 最后一个非叶子节点
        for i in range(last_father, 0, -1):
            down_adjust(arr, i, length)

    # O(logk)
    def down_adjust(arr, index, length):
        father = arr[index]
        child_index = 2 * index + 1
        while child_index < length:
            right_child = child_index + 1
            # 如果有右孩子且右孩子比左孩子小，则定位到右孩子
            if right_child < length and arr[right_child] < arr[child_index]:
                child_index += 1
            # 如果父节点小于任何一个孩子的值，直接跳出
            if father <= arr[child_index]:
                break
            # 无需真正交换，单向赋值即可
            arr[index] = arr[child_index]
            index = child_index # 记录被替换的孩子节点的位置
            child_index = 2 * child_index + 1 # 下一层的孩子节点
        arr[index] = father # 被替换的孩子节点赋值为父亲节点的值

    build_heap(arr, k) # 用前k个元素构建小顶堆
    # 继续遍历数组，和堆顶比较大小
    # O(n - k)
    for i in range(k, len(arr) - 1):
        # 找到比堆顶元素更大的值，替换并调整堆为小顶堆
        if arr[i] > arr[0]:
            arr[0] = arr[i]
            down_adjust(arr, 0, k)
    # 返回堆顶元素
    return arr[0]

# 方法四：快速排序（分治）
# O(n)
@print_run_time
def solution4(arr, k):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def partition(arr, left, right):
        pivot = left # 基准值的index
        index = pivot + 1 # 基准值的插入位置
        i = index # 移动的指针，用于比较当前位置的值与基准值的大小
        while i <= right:
            if arr[i] > arr[pivot]:
                swap(arr, i, index) # 当比基准值大，移到插入指针的左边
                index += 1 # 插入指针右移一位
            i += 1
        swap(arr, pivot, index - 1) # 遍历结束，交换基准值到插入指针的前一位
        return index - 1 # 返回当前基准值的位置

    def quick_select(arr, left, right, k):
        # 快速排序的性能和「划分」出的子数组的长度密切相关
        # 若每次都划分出n-1长度的子数组，性能退化到O(n^2)
        # 引入随机化来加速这个过程
        rand_i = random.randint(left, right)
        swap(arr, rand_i, right)
        # 左子数组元素都比基准值大，最后取当前基准值的位置，即为topk元素
        partition_index = partition(arr, left, right)
        if partition_index + 1 == k:
            return arr[partition_index]
        else:
            # 大于等于基准值的个数小于k，递归右子数组，反之递归左子数组
            if partition_index + 1 < k:
                return quick_select(arr, partition_index + 1, right, k)
            else:
                return quick_select(arr, left, partition_index - 1, k)

    return quick_select(arr, 0, len(arr) - 1, k)


if __name__ == "__main__":
    from copy import deepcopy

    arr = [7, 5, 15, 3, 17, 2, 20, 24, 1, 9, 12, 8]
    k = 3

    print(solution1(deepcopy(arr), k))
    print(solution2(deepcopy(arr), k))
    print(solution3(deepcopy(arr), k))
    print(solution4(deepcopy(arr), k))