"""
Найдите ближайшее значение к переданному.

Вам даны список значений в виде множества (Set) и значение, относительно которого, надо найти ближайшее.

Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17.
И нам нужно найти ближайшее значение к цифре 9. Если отсортировать этот ряд по возрастанию,
то слева от 9 будет 7, а справа 10. Но 10 - находится ближе, чем 7, значит правильный ответ 10.

Несколько уточнений:

Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
Ряд чисел всегда не пустой, т.е. размер >= 1;
Переданное значение может быть в этом ряде, а значит оно и является ответом;
В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
Ряд не отсортирован и состоит из уникальных чисел.
Входные данные: Два аргумента. Ряд значений в виде set. Искомое значение - int

Выходные данные: Int.

Пример:

nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
"""


def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    values = list(values)
    values.append(one)
    values.sort()
    if len(values) == 1:
        return values[0]
    elif values.index(one) == 0:
        return values[1]
    elif one == values[-1]:
        return values[-2]
    elif len(values) > 1:
        left_of_one = values.index(one) - 1
        right_of_one = values.index(one) + 1
        values = values[left_of_one:right_of_one + 1:2]
        print(values, '__')
        return values[0] if abs(values[0] - one) <= abs(values[1] - one) else values[1]


# print(nearest_value({5}, 7))

if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({-6, -2, 4, 7, 12, 17}, -4) == -6
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")
