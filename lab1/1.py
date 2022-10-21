for i in range(1, 16):
    out = i
    if i % 3 == 0:
        if i % 5 == 0:
            out = 'FizzBuzz'
        else:
            out = 'Fizz'
    elif i % 5 == 0:
        out = 'Buzz'
    print(out, end=' ' if i < 15 else '')
