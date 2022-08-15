"""
Дан непустой массив целых чисел (X). В этой задаче вам нужно вернуть массив,
состоящий только из неуникальных элементов данного массива.
Для этого необходимо удалить все уникальные элементы (которые присутствуют
в данном массиве только один раз). Для решения этой задачи не меняйте оригинальный порядок элементов.
Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].


Вх. данные: Список (list) целых чисел (int).

Вых. данные: Итератор (an iterable) целых чисел (int).

Пример:

assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
assert checkio([1, 2, 3, 4, 5]) == []
assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]

Как это используется: Эта задача поможет вам понять, как манипулировать массивами.
Это полезный базис для решения более сложных задач. Также эта идея может
быть легко обобщена для реальных задач. Для примера: если вам необходимо очистить
статистику от редко встречающихся элементов (шум).

Предусловия:
0 < len(data) < 1000
"""


def checkio(data: list) -> list:
    res = []
    for el in range(len(data)):
        if data.count(data[el]) > 1:
            res.append(data[el])
    return res


print('Example:')
print(checkio([1, 2, 3, 1, 3]))

assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
assert checkio([1, 2, 3, 4, 5]) == []
assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
assert checkio([2, 2, 3, 2, 2]) == [2, 2, 2, 2]
assert checkio([10, 20, 30, 10]) == [10, 10]
assert checkio([7]) == []
assert checkio([0, 1, 2, 3, 4, 0, 1, 2, 4]) == [0, 1, 2, 4, 0, 1, 2, 4]
assert checkio([99, 98, 99]) == [99, 99]
assert checkio([0, 0, 0, 1, 1, 100]) == [0, 0, 0, 1, 1]
assert checkio([0, 0, 0, -1, -1, 100]) == [0, 0, 0, -1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
