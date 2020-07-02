"""
堆排序和二叉堆使用的思想是一样的，第一种方法，可以先buildheap，构建二叉堆，这将花费O(N)时间，然后执行N次deleteMin操作
总的运行时间将花费O(N*logN)，每一次deleteMin都将最小值拷贝至第二个数组，但是可能在某些情况下会占用较多空间。所以可采取
第二种比较聪明的方法进行排序，可以避免这种使用第二个数组占用内存空间的方法——每次deleteMin，把最小值和末尾元素交换，再次
进行下滤时，总的deleteMin的界减小1。这将获得一个递减的序列，如果想获得递增的序列，把deleteMin换成deleteMax，得到一个
max堆就行了。所以堆排序总的思路是——
从顶点开始，先buildheap，一直到heapsize/2节点，不断往下下滤，每次下滤都把这个节点往下的左右子树中最大的值推到上面，直至
末尾，构建一个max堆，然后把顶点值和末尾值交换，从0开始下滤，每次交换值过后下滤的界减小1，直到完成排序
"""

import random


def heapsort(a):
    count = 0
    # 从heapsize/2处不断下滤，构建一个最大(最小)堆——buildheap
    for i in range((len(a)//2)-1, -1, -1):
        percdown(a, i, len(a))

    # 进行heapsize-1次下滤，完成堆排序
    for i in range(len(a)-1, -1, -1):
        swapvalue(a, 0, i)
        percdown(a, 0, i)
    print('排序后a=', a)


def swapvalue(a, start, end):
    flag = a[start]
    a[start] = a[end]
    a[end] = flag


def percdown(heaplist, hole, length):


    return heaplist


def leftchild(hole):
    if hole:
        child = hole*2
    else:
        child = hole*2+1
    return child


if __name__ == '__main__':
    a = []
    for _ in range(0, 30):
        a.append(random.randint(0, 100))
    print('排序前heaplist=', a)
    heapsort(a)