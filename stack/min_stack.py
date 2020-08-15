class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = [] # 辅助栈用于存储曾经的最小值

    def push(self, element):
        self.main_stack.append(element)
        # 若辅助栈为空或者新元素小于等于辅助栈栈顶，新元素压入辅助栈
        if len(self.min_stack) == 0 or element < self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.append(element)

    def pop(self):
        # 出栈元素与辅助栈的栈顶元素相等，辅助栈栈顶元素也出栈
        if self.main_stack[len(self.main_stack) - 1] == self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.pop()
        return self.main_stack.pop()

    def get_min(self):
        if len(self.main_stack) == 0:
            return None
        return self.min_stack[len(self.min_stack) - 1]

