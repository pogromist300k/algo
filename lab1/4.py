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


def inverse(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    a = [[a11, a12, a13],
         [a21, a22, a23],
         [a31, a32, a33]]
    inv = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]
    col = row = rk = 0
    n = 3
    while col < n and row < n:
        pivot = row
        while pivot < n and a[pivot][col] == 0:
            pivot += 1
        if pivot < n:
            rk += 1
            if pivot != row:
                switch(a[pivot], a[row])
                switch(inv[pivot], inv[row])
            sc = 1 / a[row][col]
            scal(a[row], sc)
            scal(inv[row], sc)
            for i in range(n):
                if i != row:
                    sc = -a[i][col]
                    add(a[i], a[row], sc)
                    add(inv[i], inv[row], sc)
            row += 1
        col += 1
    if rk == 3:
        return inv
    else:
        return -1


from timeit import timeit
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 4], [3, 2, 1]])
print(' Наша функция:', timeit(lambda: inverse(1, 2, 3, 4, 5, 4, 3, 2, 1), number=100))
print('Функция numpy:', timeit(lambda: np.linalg.inv(a), number=100))


