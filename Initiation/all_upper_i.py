"""
Проверить все ли символы в строке являются заглавными. Если строка пустая или в ней нет букв - функция должна вернуть True.

Входные данные: Строка.

Выходные данные: Логический тип.

Пример:
"""


def is_all_upper(text: str) -> bool:
    return True if len(text.strip()) == 0 or ''.join(text.split(' ')).isdigit() else text.isupper()
