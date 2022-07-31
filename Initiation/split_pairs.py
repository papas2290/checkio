"""
Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').

Входные данные: Строка.

Выходные данные: Массив строк.

Пример:

split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_']
"""


def split_pairs(a):
    my_list = []
    for el in range(0, len(a) - 1, 2):
        n = a[el] + a[el + 1]
        my_list.append(n)
    if len(a) % 2 != 0:
        n = a[-1] + '_'
        my_list.append(n)
    return my_list