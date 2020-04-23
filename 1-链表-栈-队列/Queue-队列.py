"""
Queue() 创建一个新的空栈
enqueue(item) 添加一个新的元素item到队列底部
delqueue() 弹出队首元素
is_empty() 判断队列是否为空
size() 返回队列的元素个数
"""


class Queue(object):

    def __init__(self):
        self.queues = []

    def is_empty(self):
        return self.queues == []

    def enqueue(self, queues):
        self.queues.append(queues)

    def delqueue(self):
        if self.is_empty():
            raise IndexError
        val = self.queues[0]
        self.queues.remove(val)
        return val

    def size(self):
        return len(self.queues)


if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    for i in range(10):
        queue.enqueue(i)
    print(queue.size())
    print(queue.delqueue())
    print(queue.delqueue())
