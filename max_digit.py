"""
У вас есть число и нужно определить какая цифра из этого числа является наибольшей.

Входные данные: Положительное целое число.

Выходные данные: Целое число (0-9).

Пример:

assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
"""


def max_digit(a: int) -> int:
    a = str(a)
    max_dig = 0
    for el in a:
        el = int(el)
        if el > max_dig:
            max_dig = el
    return max_dig
