# https://leetcode-cn.com/problems/open-the-lock/

# 将 s[j] 向上拨动一次
def plue_one(s, j):
    s = list(s)
    if s[j] == "9":
        s[j] = "0"
    else:
        s[j] = str(int(s[j]) + 1)
    return "".join(s)

# 将 s[j] 向下拨动一次
def minus_one(s, j):
    s = list(s)
    if s[j] == "0":
        s[j] = "9"
    else:
        s[j] =  str(int(s[j]) - 1)
    return "".join(s)

# BFS 框架，打印出所有可能的密码
def open_lock(deadends, target):
    # 记录需要跳过的死亡密码
    deads = set(deadends)
    # 记录已经穷举过的密码，防止走回头路
    visited = set()
    q = []

    # 从起点开始启动广度优先搜索
    step = 0
    q.append(("0000", 0))
    visited.add("0000")

    while q:
        cur, step = q.pop(0)
        if cur in deads:
            continue
        if cur == target:
            return step
        
        # 将一个节点的未遍历相邻节点加入队列
        for j in range(4):
            up = plue_one(cur, j)
            if up not in visited:
                visited.add(up)
                q.append((up, step + 1))
            down = minus_one(cur, j)
            if down not in visited:
                visited.add(down)
                q.append((down, step + 1))
    return -1

if __name__ == "__main__":
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"

    print(open_lock(deadends, target))