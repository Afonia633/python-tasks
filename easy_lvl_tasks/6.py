"""Простые числа (6)
Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
 если оно простое, и False - иначе."""
a = int(input('write 0 - 1000 '))
b = []
c = [1, a]
while True:
    for i in range(a + 1):
        if i == 0:
            continue
        elif a % i == 0:
            b.append(i)
    if b == c:
        print('True')
        break
    else:
        print('False')
        break
