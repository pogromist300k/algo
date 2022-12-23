def init():
    m = [list(map(int, input().split()))]
    for _ in range(len(m[0]) - 1):
        m.append(list(map(int, input().split())))
    return m


def print_path(m, path):
    path_set = set(path)
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j]:
                print('█', end=' ')
            else:
                print('*' if (i, j) in path_set else ' ', end=' ')
        print()


def find_path(m):
    explored = set()
    path = []

    # Поиск входа
    def find_enter():
        row = 0
        while row < len(m):
            if m[row][0] == 0:
                yield row, 0
            row += 1

    # Проверка, находимся ли мы на выходе
    def is_exit(x):
        _, col = x
        return col == len(m) - 1

    # Определение возможных направлений
    def directions(x):
        d = set()
        row, col = x
        if 0 <= col - 1 and m[row][col - 1] == 0 and not (row, col - 1) in explored:  # лево
            d.add((row, col - 1))
        if 0 <= row - 1 and m[row - 1][col] == 0 and not (row - 1, col) in explored:  # верх
            d.add((row - 1, col))
        if col + 1 < len(m) and m[row][col + 1] == 0 and not (row, col + 1) in explored:  # право
            d.add((row, col + 1))
        if row + 1 < len(m) and m[row + 1][col] == 0 and not (row + 1, col) in explored:  # низ
            d.add((row + 1, col))
        return d

    # Поиск в глубину
    def dfs(x):
        explored.add(x)
        if is_exit(x):
            path.append(x)
            return True
        for y in directions(x):
            if dfs(y):
                path.append(x)
                return True
        return False

    # Находим вход и запускаем поиск в глубину, в случае неудачи исследуем другой доступный вход
    for enter in find_enter():
        if dfs(enter):
            path.reverse()
            return path, None
    return None, "Нет входа" if len(explored) == 0 else "Нет пути"


maze = init()
path, error = find_path(maze)
if path:
    print_path(maze, path)
else:
    print(error)
