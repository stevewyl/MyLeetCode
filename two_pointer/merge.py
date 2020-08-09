from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    index1 = m - 1
    index2 = n - 1
    index_merge = m + n - 1
    while index1 >= 0 or index2 >= 0:
        if index1 < 0:
            nums1[index_merge] = nums2[index2]
            index2 -= 1
        elif index2 < 0:
            nums1[index_merge] = nums1[index1]
            index1 -= 1
        elif nums1[index1] > nums2[index2]:
            nums1[index_merge] = nums1[index1]
            index1 -= 1
        else:
            nums1[index_merge] = nums2[index2]
            index2 -= 1
        index_merge -= 1
    return nums1

if __name__ == "__main__":
    nums2 = [1, 2, 3]
    n = 3
    nums1 = [7, 8, 9] + [0] * n
    m = 3
    print(merge(nums1, m, nums2, n))