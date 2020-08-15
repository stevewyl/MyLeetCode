class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_binary_tree(input_list=[]):
    if input_list is None or len(input_list) == 0:
        return None
    data = input_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = create_binary_tree(input_list)
    node.right = create_binary_tree(input_list)
    return node

def pre_order_traversal(node):
    if node is None:
        return
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    return node

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)
    return node

def post_order_traversal(node):
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data)
    return node

def pre_order_traversal_with_stack(node):
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            print(node.data)
            stack.append(node)
            node = node.left
        if len(stack) > 0:
            node = stack.pop()
            node = node.right

def in_order_traversal_with_stack(node):
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            stack.append(node)
            node = node.left
        if  len(stack) > 0:
            node = stack.pop()
            print(node.data)
            node = node.right
        else:
            break

def post_order_traversal_with_stack(node):
    s1 = []
    s2 = []
    s1.append(node)
    while len(s1) > 0:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while len(s2) > 0:
        node = s2.pop()
        print(node.data)

if __name__ == "__main__":
    input_list = [3, 2, 9, None, None, 10, None, None, 8, None, 4]
    root = create_binary_tree(input_list)
    pre_order_traversal(root)
    print("-")
    in_order_traversal(root)
    print("-")
    post_order_traversal(root)
    print("-")
    pre_order_traversal_with_stack(root)
    print("-")
    in_order_traversal_with_stack(root)
    print("-")
    post_order_traversal_with_stack(root)