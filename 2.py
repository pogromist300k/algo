# # # Вспомогательные # # #

def input_matrix(prompt):
    print(prompt)
    m = int(input('Число строк: '))
    n = int(input('Число столбцов: '))
    a = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            a[i][j] = int(input(f'[{i + 1}][{j + 1}]: '))
    print_matrix(a)
    return a


def print_matrix(a, info='Ваша матрица:'):
    print(info)
    m, n = len(a), len(a[0])
    for i in range(m):
        for j in range(n):
            print(a[i][j], end='  ' if j < n - 1 else '\n')
    print()


def copy(a):
    m, n = len(a), len(a[0])
    b = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[i][j]
    return b


def scal(a, sc):
    m = len(a)
    for i in range(m):
        a[i] *= sc


def switch(a, b):
    m = len(a)
    for i in range(m):
        a[i], b[i] = b[i], a[i]


def add(a, b, sc):
    m = len(a)
    for i in range(m):
        a[i] += sc * b[i]


# # # Ранг (метод Гаусса) # # #

def rank(b):
    rk = 0
    a, m, n = copy(b), len(b), len(b[0])
    col = row = 0                                  # Текущие строка, столбец
    while col < n and row < m:
        pivot = row                                # Ищем строку с ведущим элементом
        while pivot < m and a[pivot][col] == 0:
            pivot += 1
        if pivot < m:                              # Если нашли
            rk += 1
            if pivot != row:                       # Перемещаем ведущую строку вверх
                switch(a[pivot], a[row])
            scal(a[row], 1 / a[row][col])          # Делаем ведущий элемент равным 1
            for i in range(row + 1, m):            # Обнуляем элементы под ведущим
                add(a[i], a[row], -a[i][col])
            row += 1
        col += 1
    return rk


# # # Транспонирование # # #

def trans(a):
    m, n = len(a), len(a[0])
    b = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[j][i]
    return b


# # # Умножение # # #

def multi(a, b):
    m, n, k = len(a), len(b[0]), len(b)
    c = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for h in range(k):
                c[i][j] += a[i][h] * b[h][j]
    return c


a = input_matrix('Инициализация матрицы')
move = input('р - Ранг\nт - Транспонирование\nу - Умножение\nДействие: ')
print()
if move == 'р':
    print('Ранг матрицы:', rank(a))

elif move == 'т':
    print_matrix(trans(a), 'Транспонированная матрица:')

elif move == 'у':
    b = input_matrix('Инициализация второй матрицы')
    if len(a[0]) == len(b):
        print_matrix(multi(a, b), 'Произведение матриц:')
    else:
        print('Ошибка: умножение невозможно')

else:
    print('Ошибка: неизвестное действие')
