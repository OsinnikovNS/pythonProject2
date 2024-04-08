# ----------- Задача 1. Динамическое определение функций. ------------
def create_operation(operation):
    if operation == "multiply":
        def multiply(x, y):
            return x * y

        return multiply
    elif operation == "division":
        def division(x, y):
            return x / y

        return division


my_func_multiply = create_operation("multiply")
print('Задача 1, ответ:', my_func_multiply(3.47, 1.735))

# --------------------  Задача 2: Лямбда-Функции.  -------------------
add = lambda x, y: x + y
print('Задача 2.1 (лямбда функция), ответ:', add(7, 9))


def add_def(x, y):
    return x + y


print('Задача 2.2 (функция def), ответ:', add_def(7, 9))


# ------------------- Задача 3: Вызываемые Объекты. --------------------
class Rect:
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        return self.a * b


area = Rect(2)
print('Задача 3, ответ:', area(4))  # Выводит площадь прямоугольника
