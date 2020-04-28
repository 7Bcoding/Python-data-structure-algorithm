import random

"""
快速排序(quick sort)的采用了分治的策略。
分治策略指的是：
将原问题分解为若干个规模更小但结构与原问题相似的子问题。递归地解这些子问题，然后将这些子问题的解组合为原问题的解。
快排的基本思想是：
在序列中找一个划分值，通过一趟排序将未排序的序列排序成 独立的两个部分，其中左边部分序列都比划分值小，右边部分的序
列比划分值大，此时划分值的位置已确认，然后再对这两个序列按照同样的方法进行排序，从而达到整个序列都有序的目的。
快速排序的时间复杂度为O(N*logN)
"""


def quickSort(a):

    quicksort(a, 0, len(a)-1)


def quicksort(a, left, right):
    if left < right:
        pivot = partition(a, left, right)
        quicksort(a, left, pivot - 1)
        quicksort(a, pivot + 1, right)


def quicksort_mid3(a, left, right):
    # 三数中值法来确定枢纽值，下标差值大于10使用快速排序，否则使用插入排序，小数组插入排序效率更高
    if left < right and (right - left) > 10:
        pivot = median3(a, left, right)
        i = left + 1
        j = right - 1
        while i < j:
            while i < j and a[i] < pivot:
                i += 1
            while i < j and a[j] > pivot:
                j -= 1
            if i < j:
                swapvalue(a, i, j)
            else:
                break
        a[i] = pivot
        # 将枢纽值两边的数组分割开，分别递归进行快速排序
        quicksort(a, i + 1, right)
        quicksort(a, left, i - 1)
    else:
        insertsort(a)


# 插入排序，用于长度小于10的小数组
def insertsort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j = i
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp
    print(a)


# 两数选出枢纽值法进行快速排序，效率比不上三数中值，但是小数组排序速度占优
def partition(a, left, right):
    pivotkey = a[left]
    while left < right:
        while left < right and a[right] >= pivotkey:
            right -= 1
        a[left] = a[right]
        while left < right and a[left] <= pivotkey:
            left += 1
        a[right] = a[left]
    a[left] = pivotkey
    return left


def median3(a, left, right):
    center = (left + right) // 2
    # 三次比较，将中间大的值作为枢纽值
    if a[center] < a[left]:
        swapvalue(a, left, center)
    if a[right] < a[left]:
        swapvalue(a, left, right)
    if a[right] < a[center]:
        swapvalue(a, right, center)
    return a[center]


def swapvalue(a, k1, k2):
    tmp = a[k1]
    a[k1] = a[k2]
    a[k2] = tmp


if __name__ == '__main__':
    a = []
    for _ in range(0, 30):
        a.append(random.randint(0, 100))
    print('排序前a=', a)
    quickSort(a)
    print('排序后a=', a)
    b = []
    for _ in range(0, 30):
        b.append(random.randint(0, 100))
    print('三数中值法排序前b=', b)
    quicksort_mid3(b, 0, len(b)-1)
    print('三数中值法排序后b=', b)



