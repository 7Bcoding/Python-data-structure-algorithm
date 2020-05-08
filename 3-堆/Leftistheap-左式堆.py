"""
左式堆：
(1)堆序性，一般左式堆都是使用最小堆（也可以实现最大堆）
对于最小堆，任意结点关键字大于或等于其父结点的关键字，也就是key(i) >= key(parent(i))。
(2)左边树更深，任意结点的左儿子零路径长大于或等于右儿子零路径长————
也就是distance(left(i)) >= distance(right(i))；任意结点的零路径长比右儿子的零路径长最小值多1，
即 distance(i)=1+distance(right(i))。
"""


class LeftistNode:
    def __init__(self, value, left, right, npl):
        self.value = value
        self.left = left
        self.right = right
        self.npl = npl


class Leftistheap:
    def __init__(self):
        self.root = None

    def merge(self, h1, h2):                # h1，h2分别表示被合并的堆和要插入的堆
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        if h1.value > h2.value:
            return self.mergeheap(h2, h1)   # h1的值大于h2的值，将h1合并入h2中
        else:
            return self.mergeheap(h1, h2)

    def mergeheap(self, h1, h2):            # h1为被合并堆，h2为插入堆
        if h1.left is None:
            h1.left = h2
        else:
            h1.right = self.merge(h1.right, h2)
            if h1.left.npl < h1.right.npl:  # 若不满足左式堆性质——左节点的npl小于右节点npl，则将左右节点交换
                self.swapchildren(h1)
            h1.npl = h1.right.npl + 1
        return h1                           # 返回被合并的h1的最终合并状态

    # 插入操作，本质是合并，将新节点创建，然后和root节点合并
    def insert(self, value):
        self.root = self.merge(LeftistNode(value), self.root)

    # 删除操作，本质也是合并，将root节点抽离，把左节点和右节点合并，即删除该元素
    def deletemin(self):
        minvalue = self.root.value
        self.merge(self.root.left, self.root.right)
        return minvalue

