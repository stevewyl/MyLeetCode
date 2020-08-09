from typing import List, Set

def permute(nums: List[int]) -> List[List[int]]:
    def dfs(nums: List[int], path: List[int], used: Set[int], res: List[List[int]]):
        # 触发结束条件
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for num in nums:
            if num in used:
                continue
            # 做选择
            used.add(num)
            path.append(num)
            # 进入下一层决策树（深度优先遍历）
            dfs(nums, path, used, res)
            # 取消选择
            used.remove(num)
            path.pop()

    res = []
    path = [] # 记录已经做出的选择
    used = set() # 选择列表
    dfs(nums, path, used, res)
    return res

if __name__ == '__main__':
    nums = [1, 2, 3]
    res_true = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
    res = permute(nums)
    print(res)