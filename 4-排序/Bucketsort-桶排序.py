import random


def bucket_sort(lst):
    buckets = [0] * ((max(lst) - min(lst))+1)
    for i in range(len(lst)):
        buckets[lst[i]-min(lst)] += 1
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+min(lst)]*buckets[i]
    return res


if __name__ == '__main__':
    a = [random.randint(0, 999) for i in range(30)]
    print("排序前...")
    print(a)
    a = bucket_sort(a)
    print("排序后...")
    print(a)
    
    
    
