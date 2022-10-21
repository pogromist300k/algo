l = 1
r = 100
count = 0
x = int(input(f'Введите число для поиска от {l} до {r}: '))
while l < r:
    count += 1
    m = (l + r) // 2
    # print(f'шаг {count}\n[{l}  {m}  {r}]')
    if x == m:
        break
    if x > m:
        l = m + 1
    else:
        r = m - 1
print('Шагов потребовалось:', count)
