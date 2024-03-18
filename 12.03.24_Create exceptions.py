# Освоить механизмы создания и обработки исключений в Python.

class ProcessingException(Exception):
    pass


class InvalidDataException(Exception):
    pass


try:
    raise ProcessingException('Исключение обработки.')
except ProcessingException as exc1:
    print(f'Конец обработки исключения ProcessingException. {exc1}')

try:
    raise InvalidDataException('Недопустимые данные.')
except InvalidDataException as exc2:
    print(f'Конец обработки исключения InvalidDataException. {exc2}')


"""Функция, которая генерирует различные исключения в зависимости
от передаваемых ей аргументов"""


def numbers(a, b):
    if b == 0:
        raise InvalidDataException
    if a < 10:
        raise ProcessingException
    return


""" Добавляем обработку исключений в функции 
и передаем исключения дальше по стеку вызовов."""

try:
    numbers(10, 5)
except ProcessingException:
    print('Исключение ProcessingException.')
except InvalidDataException:
    print('Исключение InvalidDataException.')
