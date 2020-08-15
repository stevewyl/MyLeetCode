# 二叉树的BFS

from queue import Queue

def level_order_tranversal(node):
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get() # 出队列
        print(node.data)
        # 左孩子和右孩子入队
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)