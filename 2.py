def left_binsearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        if x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return high


def right_binsearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return low


chars = ('девушка', '18-летний', 'носит очки', 'кареглазый', 'темноволосый')

students = {(0, 1, 0, 1, 1): 'Руслан Бабаев',
            (0, 1, 1, 0, 1): 'Максим Шестаков',
            (1, 0, 1, 1, 1): 'Мария Боженко',
            (0, 1, 1, 1, 1): 'Сергей Затикян',
            (1, 0, 1, 0, 0): 'Вера Шаллиева',
            (1, 0, 0, 0, 1): 'Ирина Мамзурина',
            (0, 1, 1, 0, 0): 'Илья Абдулов',
            (1, 1, 1, 0, 0): 'Екатерина Кремпольская',
            (1, 0, 0, 1, 1): 'Вера Касьяненко',
            (0, 1, 0, 0, 0): 'Александр Царёв'}

info = tuple(sorted(students.keys()))
min = [0, 0, 0, 0, 0]
max = [1, 1, 1, 1, 1]


char = 0
while char < len(chars):
    answer = input(f'Студент {chars[char]}?\n')
    if answer == 'да':
        min[char] = 1
    else:
        max[char] = 0

    l_index = right_binsearch(info, tuple(min))
    r_index = left_binsearch(info, tuple(max))

    if l_index == r_index:
        print('Вы загадали:', students[info[l_index]])
        break
    elif l_index > r_index:
        print('Такого студента нет')
        break
    char += 1
