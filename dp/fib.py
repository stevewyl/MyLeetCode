from typing import Dict

# https://leetcode-cn.com/problems/fibonacci-number/

def fib_memo(N: int) -> int:
    """
    自顶向下
    带「备忘录」的递归算法，把一棵存在巨量冗余的递归树通过「剪枝」
    时间复杂度 O(N)，每个子问题O(1), 共n个问题
    """
    def helper(memo: Dict, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        if memo.get(n, 0) != 0:
            return memo[n]
        memo[n] = helper(memo, n - 1) + helper(memo, n - 2)
        return memo[n]

    if N < 1:
        return 0
    memo = {i: 0 for i in range(N)}
    return helper(memo, N)

def fib_table(N: int) -> int:
    """
    自顶向上，dp_table
    """
    if N < 1:
        return 0
    if N == 1 or N == 2:
        return 1
    dp_table = [0] * (N + 1)
    dp_table[1] = 1
    dp_table[2] = 1
    for i in range(3, N + 1):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]
    return dp_table[N]

def fib_table_v2(N: int) -> int:
    """
    由于只需要存储前两个状态，不需要长的dp_table，空间复杂度变为O(1)
    """
    if N < 1:
        return 0
    if N == 1 or N == 2:
        return 1
    prev_1 = 1
    prev_2 = 1
    for _ in range(3, N + 1):
        current = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = current
    return current
