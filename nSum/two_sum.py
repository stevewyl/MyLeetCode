from typing import List

from linetimer import CodeTimer

# https://leetcode-cn.com/problems/two-sum/
def twoSumPointer(nums: List[int], target: int) -> List[int]:
    sorted_ids = sorted(range(len(nums)), key=lambda x: nums[x])
    l = 0
    r = len(nums) - 1
    while l < r:
        sum_tmp = nums[sorted_ids[l]] + nums[sorted_ids[r]]
        if sum_tmp < target:
            l += 1
        elif sum_tmp > target:
            r -= 1
        elif sum_tmp == target:
            break
    return [sorted_ids[l], sorted_ids[r]]

def twoSumHash(nums: List[int], target: int) -> List[int]:
    hashset = {}
    for i, num in enumerate(nums):
        if hashset.get(target - num) is not None:
            return [hashset.get(target - num), i]
        hashset[num] = i


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    with CodeTimer("pointer"):
        try:
            res = twoSumPointer(nums, target)
            assert res == [1, 2]
        except:
            print(res)
    with CodeTimer("hash"):
        try:
            res = twoSumHash(nums, target)
            assert res == [1, 2]
        except:
            print(res)
