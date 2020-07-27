from typing import List

# https://leetcode-cn.com/problems/coin-change/

def coinChange(coins: List[int], amount: int):

    def dp(n):
        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1
        # 求最小值，所以初始化为正无穷
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            # 子问题无解，跳过
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)

        return res if res != float('INF') else -1

    return dp(amount)

def coinChangeMemo(coins: List[int], amount: int):
    memo = {}

    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float("INF")
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)
        memo[n] = res if res != float("INF") else -1
        return memo[n]

    return dp(amount)

def coinChangeTable(coins: List[int], amount: int):
    dp = [float('INF')] * (amount + 1)
    dp[0] = 0
    for i in range(amount): # 枚举硬币种数
        for c in coins: # 从小到大枚举金额，确保i-c >= 0
            if i - c < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - c])
    return dp[amount] if dp[amount] != float("INF") else -1 # 如果为inf说明状态不可达，返回-1即可。
