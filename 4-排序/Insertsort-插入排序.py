"""
插入排序，也称为冒泡排序，从1到len(list)，倒序循环，不断交换相邻元素，较小（大）的顶到前面，时间复杂度O(N^2)
"""


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
    a = [3, 4, 8, 54, 23, 76, 65, 33, 982, 235, 323]
    insertsort1(a)
