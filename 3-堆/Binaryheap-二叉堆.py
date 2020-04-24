import random


class Binaryheap:
    def __init__(self, heapsize, heaplist=[]):
        self.currentsize = heapsize
        self.heaplist = heaplist

    # 构建一个二叉堆
    def Binaryheap(self, hlist):
        self.currentsize = len(hlist)
        self.heaplist = []
        for i in range(self.currentsize):
            self.heaplist[i] = hlist[i]
        self.buildheap()

    def buildheap(self):

        for i in range(self.currentsize/2, 0, -1):
            self.percolatedown(i)

    # 插入一个值
    def insert(self, value):
        hole = self.currentsize + 1
        self.heaplist[0] = value
        while hole > 0:
            # 插入的值大于空洞位置的父节点，则作为父节点的子节点插入
            if value > self.heaplist[hole/2]:
                break
            else:
                # 小于父节点，则把父节点移至空洞位置（作为子节点），并将空洞推至父节点位置，继续循环
                self.heaplist[hole] = self.heaplist[hole/2]
                hole = hole / 2
        self.heaplist[hole] = value

    def deleteMin(self):
        minvalue = self.findMin()
        self.heaplist[0] = self.heaplist[self.currentsize-1]
        self.percolatedown(1)
        return minvalue

    # 从某个节点开始下滤，梳理堆的大小顺序，更小的值会顶到上面
    def percolatedown(self, hole):
        # 从hole所处的节点开始下滤
        tmp = self.heaplist[hole]
        while hole * 2 <= self.currentsize:
            minheap = hole*2
            if hole * 2 != self.currentsize and (self.heaplist[hole*2] < self.heaplist[hole*2+1]):
                    # 比较左右两个节点，更小的值赋给minheap
                    minheap = hole*2+1
            # 比较minheap和tmp大小，若小于，将minheap推上父节点，反之将tmp推至父节点
            if self.heaplist[minheap] < tmp:
                self.heaplist[hole] = self.heaplist[minheap]
            else:
                break
            # 每次都将hole下移至原minheap的位置，继续比较出hole的子节点的更小值
            hole = minheap
        self.heaplist[hole] = tmp


if __name__ == '__main__':
    heaparray = []
    for i in range():
        heaparray.append(random.randint(0, 1000))
    binaryheap = Binaryheap(heaparray)
    binaryheap.buildheap()

