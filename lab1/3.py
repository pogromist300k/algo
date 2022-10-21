import numpy as np


def input_matrix(prompt):
    print(prompt)
    m = int(input('Число строк: '))
    n = int(input('Число столбцов: '))
    a = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            a[i][j] = int(input(f'[{i + 1}][{j + 1}]: '))
    a = np.array(a)
    print('Ваша матрица:\n', a, end='\n\n')
    return a


a = input_matrix('Инициализация матрицы')
move = input('р - Ранг\nт - Транспонирование\nу - Умножение\nДействие: ')
print()
if move == 'р':
    print('Ранг матрицы:', np.linalg.matrix_rank(a))

elif move == 'т':
    print('Транспонированная матрица:\n', np.transpose(a))

elif move == 'у':
    b = input_matrix('Инициализация второй матрицы')
    if len(a[0]) == len(b):
        print('Произведение матриц:\n', np.dot(a, b))
    else:
        print('Ошибка: умножение невозможно')

else:
    print('Ошибка: неизвестное действие')
