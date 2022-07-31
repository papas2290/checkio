"""
Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий.

Это упрощенная версия миссии Between Markers .

Начальный и конечный маркеры всегда разные.
Начальный и конечный маркеры всегда размером в один символ.
Начальный и конечный маркеры всегда есть в строке и идут один за другим.
Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.

Output: Строка.

Пример:

assert between_markers('What is >apple<', '>', '<') == 'apple'
assert between_markers('What is [apple]', '[', ']') == 'apple'
assert between_markers('What is ><', '>', '<') == ''
assert between_markers('[an apple]', '[', ']') == 'an apple'
"""


def between_markers(text: str, start: str, end: str) -> str:
    marker_start = text.index(start)
    marker_end = text.index(end)
    return text[marker_start + 1:marker_end]
