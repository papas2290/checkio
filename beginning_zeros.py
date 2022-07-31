"""
Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки.

Входные данные: Строка, состоящая только из цифр.

Выходные данные: Целое число.

Пример:

assert beginning_zeros('100') == 0
assert beginning_zeros('001') == 2
assert beginning_zeros('100100') == 0
assert beginning_zeros('001001') == 2
"""


def beginning_zeros(a: str) -> int:
    count_0 = ''
    for el in a:
        if el == '0':
            count_0 += el
        else:
            return len(count_0)
    return len(count_0)
