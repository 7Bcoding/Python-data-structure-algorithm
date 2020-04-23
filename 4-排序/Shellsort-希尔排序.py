# 希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本,
# 该方法的基本思想是：先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序，
# 然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）时，再对全体元素进行一次直接插入排序。
# 因为直接插入排序在元素基本有序的情况下（接近最好情况），效率是很高的，因此希尔排序在时间效率比直接插入排序有较大提高。


def shellsort1(a):
    global step
    step = (len(a) - 1) // 2
    while step > 0:
        for i in range(step, len(a)):
            tmp = a[i]
            flag = i
            for j in range(i, step-1, -step):
                if tmp < a[j-step]:
                    a[j] = a[j-step]
                    flag = j-step
            a[flag] = tmp
        step = step // 2
    print('final a=', a)


def shellsort2(a):
    b = len(a)  # 列表长度
    step = b // 2  # 初始步长设置为总长度的一半
    while step >= 1:
        for i in range(b):
            tmp = a[i]
            j = i
            while j >= step and a[j - step] > a[j]:  # 在每一组里面进行直接插入排序
                a[j] = a[j - step]
                j -= step
            a[j] = tmp
        step = step // 2  # 更新步长
    print(a)


if __name__ == '__main__':
    a = [99, 52, 87, 65, 98, 1, 3, 55, 14, 32, 287, 54, 6, 95, 43, 13, 7, 23]
    shellsort1(a)
    shellsort2(a)