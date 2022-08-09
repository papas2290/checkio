"""
Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом.
Если число является частью слова, то его суммировать не нужно.

Текст состоит из чисел, пробелов и букв английского алфавита.

Входные данные: Строка.

Выходные данные: Целое число.

Пример:

sum_numbers('hi') == 0
sum_numbers('who is 1st here') == 0
sum_numbers('my numbers is 2') == 2
sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
sum_numbers('5 plus 6 is') == 11
sum_numbers('') == 0
"""


def sum_numbers(text: str) -> int:
    my_list = text.split(' ')
    my_list_int = []
    for el in my_list:
        if el.isdigit():
            my_list_int.append(int(el))
    return sum(my_list_int)


if __name__ == "__main__":
    print("Example:")
    print(sum_numbers("hi"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers("hi") == 0
    assert sum_numbers("who is 1st here") == 0
    assert sum_numbers("my numbers is 2") == 2
    assert (
            sum_numbers(
                "This picture is an oil on canvas "
                "painting by Danish artist Anna "
                "Petersen between 1845 and 1910 year"
            )
            == 3755
    )
    assert sum_numbers("5 plus 6 is") == 11
    assert sum_numbers("") == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
