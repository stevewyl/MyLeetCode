from typing import List

from linetimer import CodeTimer

def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int(left + (right - left) / 2) # 防止left和right相加太大数值溢出
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1

def left_bound(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    # 搜索空间为[left, right]
    while left <= right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            # 收缩右侧边界
            right = mid - 1
        elif nums[mid] < target:
            # 搜索区间变为[mid+1, right]
            left = mid + 1
        elif nums[mid] > target:
            # 搜索区间变为[left, mid-1]
            right = mid - 1
    # 检查出界情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left

def right_bound(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    # 搜索空间为[left, right]
    while left <= right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            # 收缩左侧边界
            left = mid + 1
        elif nums[mid] < target:
            # 搜索区间变为[mid+1, right]
            left = mid + 1
        elif nums[mid] > target:
            # 搜索区间变为[left, mid-1]
            right = mid - 1
    if right < 0 or nums[right] != target:
        return -1
    return right

def searchRange(nums: List[int], target: int) -> List[int]:
    lr = left_bound(nums, target)
    if lr == -1:
        return [-1, -1]
    else:
        rr = right_bound(nums[lr + 1:], target)
        return [lr, lr + 1 + rr]


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    with CodeTimer("binary_search"):
        index = search(nums, target)
        assert index == 4

    nums = [1]
    target = 1
    with CodeTimer("search_range"):
        idx_range = searchRange(nums, target)
        assert idx_range == [0, 0]