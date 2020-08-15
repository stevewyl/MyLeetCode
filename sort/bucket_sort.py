def bucket_sort(array=[]):
    # 得到最大值、最小值和差值
    max_v = array[0]
    min_v = array[1]
    for i in range(1, len(array)):
        if array[i] > max_v:
            max_v = array[i]
        if array[i] < min_v:
            min_v = array[i]
    d = max_v - min_v
    # 初始化桶
    bucket_num = len(array)
    bucket_list = []
    for i in range(0, bucket_num):
        bucket_list.append([])
    # 遍历数组，元素入桶
    for i in range(0, len(array)):
        num = int((array[i] - min_v) * (bucket_num - 1) / d)
        bucket = bucket_list[num]
        bucket.append(array[i])
    # 每个桶内部进行排序
    for i in range(0, len(bucket_list)):
        bucket_list[i].sort()
    # 输出全部元素
    sorted_array = []
    for sub_list in bucket_list:
        for element in sub_list:
            sorted_array.append(element)
    return sorted_array

if __name__ == "__main__":
    my_array = [4.12, 6.421, 0.0023, 3.0, 2.133, 8.122, 4.12, 10.99]
    print(bucket_sort(my_array))
