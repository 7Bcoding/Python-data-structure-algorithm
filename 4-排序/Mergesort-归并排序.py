"""
归并排序其实是分治算法思想的一种，递归的将数组的前半部分和后半部分各自进行归并排序，梳理好顺序后，再
将两个数组用合并算法合并到一起，很显然，分而治之，"分"到最后最小的数组————左右数组都是一个元素，然后再
"治"之，递归向上合并排序结果。
归并排序用到的时间复杂度为O(NlogN)，所用到的比较次数几乎是最优的。但是在合并算法中会开启一个tmp数组，
占用较多的空间，并且每次从tmp拷贝回原数组都会消耗一些时间，减慢排序速度

"""
import random


def mergeSort(a):
    tmparray = [0] * len(a)
    mergesort(a, tmparray, 0, len(a)-1)
    print('排序后a=', a)


def mergesort(a, tmpA, left, right):

    if left < right:
        center = (left + right) // 2
        mergesort(a, tmpA, left, center)
        mergesort(a, tmpA, center+1, right)
        merge(a, tmpA, left, center+1, right)


def merge(a, tmpA, lpos, rpos, rend):
    lend = rpos - 1
    tmppos = lpos
    lengthA = rend - lpos + 1
    while lpos <= lend and rpos <= rend:
        if a[lpos] <= a[rpos]:
            tmpA[tmppos] = a[lpos]
            tmppos += 1
            lpos += 1
        else:
            tmpA[tmppos] = a[rpos]
            tmppos += 1
            rpos += 1
    while lpos <= lend:
        tmpA[tmppos] = a[lpos]
        tmppos += 1
        lpos += 1
    while rpos <= rend:
        tmpA[tmppos] = a[rpos]
        tmppos += 1
        rpos += 1
    for _ in range(0, lengthA):
        a[rend] = tmpA[rend]
        rend -= 1


if __name__ == '__main__':
    a = []
    for _ in range(0, 30):
        a.append(random.randint(0, 100))
    print('排序前a=', a)
    mergeSort(a)
    
    
    
