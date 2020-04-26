import random


def quickSort(a):
    quicksort(a, 0, len(a)-1)


def quicksort(a, left, right):

    # 三数中值法来确定枢纽值
    pivot = median3(a, left, right)
    i = left+1
    j = right-2
    while 1:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i < j:
            swapvalue(a, i, j)
        else:
            break
    # 枢纽值位于right-1位置，将枢纽值与i最后停留的值进行交换
    # i最后停留的值为最后一个大于pivot的值，位于分割数组的中间位置
    swapvalue(a, i, right-1)
    print(a)
    print('i= %d, j= %d, i-1= %d, ' % (i, j))
    # 将枢纽值两边的数组分割开，分别递归进行快速排序
    if i<len(a) and j>0:
        quicksort(a, i+1, right)
        quicksort(a, left, i-1)


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
    swapvalue(a, center, right-1)
    return a[right-1]


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


