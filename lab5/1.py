# Возвращает 0, если str есть правильная скобочная последовательность (correct brackets sequence)
# или пустая строка, в ином случае — номер первого нарущающего корректность символа
def cbs(str):
    stack = []
    for i in range(len(str)):
        if str[i] == '(':
            stack.append('(')
        elif str[i] == ')' and len(stack) != 0:
            stack.pop()
        else:
            return i + 1
    return 0 if len(stack) == 0 else len(str)


while True:
    str = input("Введите строку: ")
    if str == 'stop':
        break
    res = cbs(str)
    print(f"НЕТ: {res}" if res > 0 else "НЕТ: пустая строка" if len(str) == 0 else "ДА")
