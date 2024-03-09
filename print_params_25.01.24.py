# Функция с параметрами по умолчанию:

def print_params(a=1, b='строка', c=True):
    return (a, b, c)

print(print_params(a=100))
# Вызов функции print_params с аргументом b=25:
print(print_params(b=25))
# Вызов функции print_params с аргументом c = [1,2,3]:
print(print_params(c=[1,2,3]))
# Вызов функции print_params без аргументов:
print(print_params())

# "Распаковка параметров:"
def vector(x, y, z):
    return (x, y, z)

values_list = [3, 'stroka', True]
print(vector(*values_list))

values_dict = {'x': 10, 'y': 'строка', 'z': True}
print(vector(**values_dict))

# Распаковка + отдельные параметры:
values_list_2 = [11, 'строка']
print(print_params(*values_list_2, 42))
# Распаковка + отдельные параметры - работает
