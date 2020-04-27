import random


def quickSort(a):

    quicksort(a, 0, len(a)-1)


def quicksort(a, left, right):
    if left < right:
        pivot = partition(a, left, right)
        quicksort(a, left, pivot - 1)
        quicksort(a, pivot + 1, right)


def quicksort_mid3(a, left, right):
    # 三数中值法来确定枢纽值
    if left < right and (right - left) >= 10:
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


def insertsort(alist):

    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                 tmp = alist[j]
                 alist[j] = alist[j-1]
                 alist[j-1] = tmp
            else:
                continue
    print(alist)


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
    # 将枢纽值放置在数组的倒数第2个位置（交换完毕再将枢纽值放到两边数组中间）
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



