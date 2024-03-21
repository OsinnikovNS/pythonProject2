"""Напишите функцию-генератор all_variants, которая будет возвращать
все подпоследовательности переданной строки.
В функцию передаётся только сама строка."""


def all_variants(text):
    for x in range(len(text)):
        yield text[x]
    for x in range(len(text)-1):
        for y in range(x+2, len(text)):
            yield text[x:y]
    for x in range(1, len(text)):
        for y in range(x+2, len(text)+1):
            yield text[x:y]
    yield text


a = all_variants("abc")
for i in a:
    print(i)


# def all_variants(text):
#     for x in range(len(text)):
#         for y in range(x+1, len(text)+1):
#             yield text[x:y]
#
#
# a = all_variants("abc")
# for i in a:
#     print(i)
