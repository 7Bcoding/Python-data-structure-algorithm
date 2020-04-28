import random

"""
所谓冒泡排序，就是将元素两两之间进行比较，谁大就往后移动，直到将最大的元素排到最后面，
接着再循环一趟，从头开始进行两两比较，而上一趟已经排好的那个元素就不用进行比较了。
"""


def bubblesort(a):

    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                continue


# 冒泡排序优化一：
# 设定一个变量为False，如果元素之间交换了位置，将变量重新赋值为True,最后再判断，
# 在一次循环结束后，变量如果还是为False，则brak退出循环，结束排序。
def bubblesort1(a):
    for i in range(len(a) - 1):
        flag = False
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = True
        if not flag:
            break


# 冒泡排序优化二：搅拌排序 / 鸡尾酒排序
# 考虑当最大值和最小值分别在两端的情况。写成双向排序提高效率，即当一次从左向右的排序
# 比较结束后，立马从右向左来一次排序比较。
def bubblesort2(items):
    for i in range(len(items) - 1):
        flag = False
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                flag = True
        if flag:
            flag = False
            for j in range(len(items) - 2 - i, 0, -1):
                if items[j - 1] > items[j]:
                    items[j], items[j - 1] = items[j - 1], items[j]
                    flag = True
        if not flag:
            break
    return items


if __name__ == '__main__':
    a = []
    b = []
    c = []
    for _ in range(0, 30):
        a.append(random.randint(0, 100))
    print('排序前a=', a)
    bubblesort(a)
    print('排序后a=', a)
    for _ in range(0, 30):
        b.append(random.randint(0, 100))
    print('排序前a=', b)
    bubblesort1(b)
    print('排序后a=', a)
    for _ in range(0, 30):
        c.append(random.randint(0, 100))
    print('排序前a=', c)
    bubblesort2(c)
    print('排序后a=', c)
