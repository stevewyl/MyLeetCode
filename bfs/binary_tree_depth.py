# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    q = [root]
    # root本身是一层， depth初始化为1
    depth = 1

    while q:
        print(q)
        for i in range(len(q)):
            cur = q.pop(0)
            # 到达叶子节点
            if not cur.left and not cur.right:
                return depth
            # 将cur的相邻节点加入队列
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        depth += 1
    return depth

if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]
    print(minDepth(root))
