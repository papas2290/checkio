"""
Попробуйте выяснить какое количество нулей содержит данное число в конце.

Входные данные: Положительное целое число (int).

Выходные данные: Целое число (int).

Пример:
"""


def end_zeros(a: int) -> int:
    a = str(a)[::-1]
    count = 0
    for el in a:
        n = int(el)
        if n == 0:
            count += 1
        else:
            break
    return count
