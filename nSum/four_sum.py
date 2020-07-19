from typing import List

from linetimer import CodeTimer

# https://leetcode-cn.com/problems/4sum

def twoSum(nums: List[int], start: int, target: int) -> List[List[int]]:
    """
    O(N)
    """
    l = start
    r = len(nums) - 1
    result = []
    while l < r:
        left = nums[l]
        right = nums[r]
        sum_tmp = left + right
        if sum_tmp < target:
            while l < r and nums[l] == left:
                l += 1
        elif sum_tmp > target:
            while l < r and nums[r] == right:
                r -= 1
        else:
            result.append([left, right])
            while l < r and nums[l] == left:
                l += 1
            while l < r and nums[r] == right:
                r -= 1
    return result

def threeSum(nums: List[int], start: int, target: int) -> List[List[int]]:
    """
    O(NlogN + N^2) = O(N^2)
    """
    nums.sort() # O(NlogN)
    n = len(nums)
    result = []
    i = start
    while i < n: # O(N)
        two_sum_res = twoSum(nums, i + 1, target - nums[i]) # O(N)
        for res in two_sum_res:
            res = [nums[i]] + res
            result.append(res)
        while i < n - 1 and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return result

def fourSum(nums: List[int], start: int, target: int) -> List[List[int]]:
    """O(N^3)"""
    nums.sort() # O(NlogN)
    n = len(nums)
    result = []
    i = 0
    while i < n: # O(N)
        three_sum_res = threeSum(nums, i + 1, target - nums[i]) # O(N^2)
        for res in three_sum_res:
            res = [nums[i]] + res
            result.append(res)
        while i < n - 1 and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return result


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    with CodeTimer("four_sum"):
        try:
            res = fourSum(nums, 0, target)
            assert res == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        except:
            print(res)