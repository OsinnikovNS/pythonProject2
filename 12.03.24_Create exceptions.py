# Освоить механизмы создания и обработки исключений в Python.
# Функция, которая генерирует различные исключения в зависимости
# от передаваемых ей аргументов

class ProcessingException(Exception):
    pass


try:
    raise ProcessingException('Это мое собственное исключение обработки.')
except ProcessingException as exc1:
    print(f'Конец обработки исключения ProcessingException. {exc1}')


class InvalidDataException(Exception):
    pass


try:
    raise InvalidDataException('Недопустимые данные.')
except InvalidDataException as exc2:
    print(f'Конец обработки исключения InvalidDataException. {exc2}')


# while True:
#     try:
#         x = int(input("Пожалуйста введите данные: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
def numbers(a, b):
    if b == 0:
        raise ProcessingException
    return a / b


try:
    res = numbers(10, 2)
except ProcessingException as e:
    print(f"Сообщение об ошибке: {e}")

# a = float(input())
# if a == 0:
#     print('Обратного числа не существует')
# else:
#     print(1/a)
