from typing import List

from linetimer import CodeTimer

def nSumTarget(nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
    result = []
    nl = len(nums)
    i = start
    if n < 2 or nl < n:
        return result
    if n == 2:
        l = start
        r = nl - 1
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
    else:
        while i < nl:
            sub_result = nSumTarget(nums, n - 1, i + 1, target - nums[i])
            for res in sub_result:
                res = [nums[i]] + res
                result.append(res)
            while i < nl - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
    return result

def nSum(nums: List[int], n: int, target: int) -> List[List[int]]:
    nums.sort()
    return nSumTarget(nums, n, 0, target)

if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    n = 4
    target = 0
    with CodeTimer("n_sum"):
        try:
            res = nSum(nums, n, target)
            assert res == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        except:
            print(res)
