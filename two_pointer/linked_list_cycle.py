# 方法一：辅助空间
# 时间复杂度O(N), 空间复杂度O(N)
def hasCycle1(head: ListNode) -> bool:
    visited = set()

    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False

# 方法二：快慢指针
def hasCycle2(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
