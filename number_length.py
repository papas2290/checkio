"""
Вам дано положительное целое число. Определите сколько цифр оно имеет.

Входные данные: Положительное целое число

Выходные данные: Целое число.

Пример:

assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2
"""


def number_length(a: int) -> int:
    return len(str(a))
