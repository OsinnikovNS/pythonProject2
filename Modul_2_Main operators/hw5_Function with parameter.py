# Домашняя работа по уроку "Функции в Python. Функция с параметром"
# Создаем функцию def print_params, которая в своем теле
# будет распечатывать переданное значение из параметра 2 раза!
def print_params(param):
    print('Печать функции первый раз:', param)
    print('Печать функции второй раз:', param)


spisok = ['параметр 1', 'параметр 2']

# выполнение функции в диапазоне
for element in spisok:
    print_params(param=element)
print('Конец цикла.')

# проба
# def power(number, pow1):
#     print('Функция с параметром', number, pow1)
#     power_v = number ** pow1
#     return power_v
#
# my_list = (3, 5, 7, 9)
# for element in my_list:
#     result = power(number=element, pow1=3)
#     print(result)
