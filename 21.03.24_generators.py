"""Напишите функцию-генератор all_variants, которая будет возвращать
все подпоследовательности переданной строки.
В функцию передаётся только сама строка."""


def all_variants(text):
    for x in range(len(text)):
        for y in range(x+1, len(text)+1):
            yield text[x:y]


a = all_variants("abc")
for i in a:
    print(i)
