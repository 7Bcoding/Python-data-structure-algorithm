import random

"""
选择排序:每次一轮遍历都找到当前最小的元素并和未排序元素的第一个元素交换位置
"""


def selectionsort(arr):

    for i in range(len(arr) - 1):                        # 第一层for表示循环选择的遍数
        min_index = i                                    # 将起始元素设为最小元素
        for j in range(i + 1, len(arr)):                 # 第二层for表示最小元素和后面的元素逐个比较
            if arr[j] < arr[min_index]:                  # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]  # 查找一遍后将最小元素与起始元素互换
    return arr


if __name__ == '__main__':
    a = []
    for _ in range(0, 30):
        a.append(random.randint(0, 100))
    print('排序前a=', a)
    selectionsort(a)
    print('排序后a=', a)


