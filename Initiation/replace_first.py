"""
В данном списке первый элемент должен стать последним. Пустой список
или список из одного элемента не должен измениться.

Входные данные: Список.

Выходные данные: Набор элементов.

Пример:

replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
replace_first([1]) == [1]
"""

from typing import Iterable


def replace_first(items: list) -> Iterable:
    try:
        if len(items) == 0 or len(items) == 1:
            return items
        else:
            first_el = items.pop(0)
            items.append(first_el)
            return items

    except Exception as e:
        return f'{e}'
