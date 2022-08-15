"""
Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
затем перемножить эту сумму и последний элемент исходного массива. Не забудьте,
что первый элемент массива имеет индекс 0.

Для пустого массива результат всегда 0 (ноль).

Входные данные: Список (list) целых чисел (int).

Выходные данные: Число как целочисленное (int).

Примеры:

assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

Зачем это нужно: Индексы и срезы - очень важные элементы программирования,
как на Python, так и на других языках. Это поможет вам в дальнейшем.

Предусловия: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
"""


def checkio(array: list[int]) -> int:
    if len(array) == 0:
        return 0
    else:
        my_list = []
        for el in range(len(array)):
            if el % 2 == 0:
                my_list.append(array[el])
        return sum(my_list) * array[-1]


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
