"""
插入排序，也称为冒泡排序，从1到len(list)，倒序循环，不断交换相邻元素，较小（大）的顶到前面，时间复杂度O(N^2)
"""
import random


def insertsort1(alist):

    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                 tmp = alist[j]
                 alist[j] = alist[j-1]
                 alist[j-1] = tmp
            else:
                continue
    print(alist)


def insertsort2(blist):

    for i in range(1, len(blist)):
        tmp = blist[i]
        for j in range(i, 0, -1):
            if blist[j] < blist[j-1]:
                blist[j] = blist[j-1]
            else:
                continue
        blist[j] = tmp
    print(blist)


if __name__ == '__main__':
    a = []
    for _ in range(0, 30):
        a.append(random.randint(0, 100))
    insertsort1(a)
    insertsort2(a)
