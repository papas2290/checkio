"""
Дана строка и нужно найти ее первое слово.

Это упрощенная версия миссии First Word , которую можно решить позднее.

Строка состоит только из английских символов и пробелов.
В начале и в конце строки пробелов нет.
Входные данные: строка (str).

Выходные данные: строка (str).

Пример:

assert first_word('Hello world') == 'Hello'
assert first_word('a word') == 'a'
assert first_word('greeting from CheckiO Planet') == 'greeting'
assert first_word('hi') == 'hi'
"""


def first_word(text: str) -> str:
    return text.split(' ')[0]
