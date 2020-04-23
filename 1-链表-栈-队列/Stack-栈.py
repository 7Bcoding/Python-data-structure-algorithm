"""
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
"""


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # 入栈
    def push(self, item):
        self.items.append(item)

    # 弹出栈顶
    def pop(self):
        if self.is_empty():
            raise IndexError
        self.items.pop()

    # 返回栈顶元素
    def peek(self):
        return self.items[self.size()-1]

    # 获取栈长度
    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()
    for i in range(0, 10):
        stack.push(i)
    print(stack.size())
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    print(stack.peek())

