"""
У вас есть последовательность строк, и вы хотите определить наиболее часто встречающуюся строку в последовательности. Он может быть только один.

Вход: непустой список строк.

Выход: строка.

Пример:
most_frequent([
    'a', 'b', 'c',
    'a', 'b',
    'a'
]) == 'a'
most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
"""


def most_frequent(data: list) -> str:
    count = 0
    elem = None
    for el in data:
        i = data.count(el)
        if i > count:
            count = i
            elem = el
    return f'{elem}'
