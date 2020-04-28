import random


def bubblesort(a):

    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                continue
    print(a)


if __name__ == '__main__':
    a = []
    for _ in range(0, 30):
        a.append(random.randint(0, 100))
    print('排序前a=', a)
    bubblesort(a)