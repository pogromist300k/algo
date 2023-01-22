import timeit
import random
import sortings as s

while True:
    usr_input = input('range, size: ')
    if usr_input == 'stop':
        break
    sorting = input('sorting: ')
    print_list = input('display the list: ')

    min, max, n = map(int, usr_input.split())
    a = [random.randint(min, max) for _ in range(n)]

    if sorting == 'quick':
        time = timeit.timeit(lambda: s.quick_sort(a, 0, len(a)), number=1)
    elif sorting == 'comb':
        time = timeit.timeit(lambda: s.comb_sort(a), number=1)

    print('\n', sorting.upper(), '-SORT', sep='')
    if print_list == 'yes':
        for i in range(len(a)):
            print(a[i], end=' ' if i < len(a) - 1 else '\n')
    print('time: ', round(time, 5), '\n')
