# Освоить механизмы создания и обработки исключений в Python.
# Функция, которая генерирует различные исключения в зависимости
# от передаваемых ей аргументов

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


def numbers(a, b):
    if b == 0:
        raise InvalidDataException
    # return a / b
    if a < 10:
        raise ProcessingException
    return a / b


try:
    res = numbers(10, 0)
except ProcessingException:
    print('Исключение ProcessingException.')
except InvalidDataException:
    print('Исключение InvalidDataException.')
