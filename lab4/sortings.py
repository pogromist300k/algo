import random


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


# QUICK-SORT #
def quick_sort(a, l, r):

    def partition(pivot):
        swap(a, l, pivot)
        pivot = l
        big = l + 1
        for i in range(l + 1, r):
            if a[i] <= a[pivot]:
                if a[i] < a[pivot]:
                    swap(a, i, pivot)
                    pivot += 1
                swap(a, i, big)
                big += 1
        return pivot, big

    if r - l > 1:
        r2, l2 = partition(random.randint(l, r - 1))
        quick_sort(a, l, r2)
        quick_sort(a, l2, r)


# COMB-SORT #
def comb_sort(a):
    step = len(a)
    inv_count = [0, 0]
    while step > 1 or inv_count[0] != inv_count[1]:
        if step > 1:
            step = int(step / 1.247)
        inv_count[0] = inv_count[1]
        for i in range(len(a) - step):
            if a[i] > a[i + step]:
                inv_count[1] += 1
                swap(a, i, i + step)
    return inv_count[0]
