# Произвольное число позиционных параметров
def test(*args):
    print('test')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)

test(10, 'Привет', 11.1, 4, 7, 9)


# рекурсивная функция, которая считает факториал от числа n
def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n

n = int(input('Введите число n:'))
print(factorial(n))
