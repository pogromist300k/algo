import random
import timeit
# import sortings as s


# BUBBLE-SORT #
def bubble_sort(a):
    sorted = 0
    inv_count = [None, 0]
    while sorted < len(a) - 1 and inv_count[0] != inv_count[1]:
        inv_count[0] = inv_count[1]
        for i in range(len(a) - 1 - sorted):
            if a[i] > a[i + 1]:
                inv_count[1] += 1
                a[i], a[i + 1] = a[i + 1], a[i]
        sorted += 1
    return inv_count[1]


# CORRECTNESS CHECK #
print('CORRECTNESS')
a = [random.randint(-100, 100) for _ in range(20)]
print(a)
bubble_sort(a)
print('after bubble_sort', a, '', sep='\n')

# TIME CHECK #
for k in [1, 3, 5, 7, 9, 11]:
    a = [random.randint(-10_000, 10_000) for _ in range(k * 1000)]

    bubble_time = timeit.timeit(lambda: bubble_sort(a.copy()), number=1)
    sort_time = timeit.timeit(lambda: a.copy().sort(), number=1)
    # bubble_inversons = bubble_sort(a.copy())
    # comb_inversions = s.comb_sort(a.copy())

    print(f'       SIZE {k * 1000}')
    print('          TIME')
    print('bubble            ', round(bubble_time, 5))
    print('  sort            ', round(sort_time, 5))
    # print('       INVERSIONS')
    # print('bubble            ', bubble_inversons)
    # print('  comb            ', comb_inversions)
    print()
