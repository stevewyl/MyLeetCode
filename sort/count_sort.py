def count_sort_v1(array=[]):
    # 取最值
    max_v = array[0]
    for i in range(1, len(array)):
        if array[i] > max_v:
            max_v = array[i]
    # 初始化计数数组
    count_arr = [0] * (max_v + 1)
    # 遍历数组，获取频数
    for i in range(0, len(array)):
        count_arr[array[i]] += 1
    # 输出排序结果
    sorted_array = []
    for i, cnt in enumerate(count_arr):
        sorted_array.extend([i] * cnt)
    return sorted_array

# 改进点一：优化计数数组的空间开销
# 改进点二：变为稳定排序
def count_sort_v2(array=[]):
    max_v = array[0]
    min_v = array[0]
    for i in range(1, len(array)):
        if array[i] > max_v:
            max_v = array[i]
        if array[i] < min_v:
            min_v = array[i]
    d = max_v - min_v # 区间缩放
    count_arr = [0] * (d + 1)
    for i in range(0, len(array)):
        count_arr[array[i] - min_v] += 1
    # 得到每个相同元素的最大下标范围
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    sorted_array = [0] * len(array)
    for i in range(len(array) - 1, -1, -1):
        new_v = array[i] - min_v
        sorted_array[count_arr[new_v]-1] = array[i]
        count_arr[new_v] -= 1
    return sorted_array


if __name__ == "__main__":
    from IPython import get_ipython
    ipython = get_ipython()

    my_array = [4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10]
    ipython.magic("%timeit count_sort_v1(my_array)") # 4.4us
    ipython.magic("%timeit count_sort_v2(my_array)") # 6.82us

    my_array = [95, 94, 91, 98, 99, 90, 99, 93, 91, 92]
    ipython.magic("%timeit count_sort_v1(my_array)") # 16us
    ipython.magic("%timeit count_sort_v2(my_array)") # 5.84us
