""" Задание.
1. Импортируйте модуль warnings.
2. Реализуйте функцию для расчёта деления, которая будет генерировать
предупреждение, если делитель близок к нулю (например, меньше 0.01),
предупреждая об опасности деления на 0.
3. Сгенерируйте UserWarning в этом случае.
4. Используйте разные фильтры для управления поведением программы при
появлении такого предупреждения: always, ignore, error
"""
import warnings  # Импорт модуля warnings


def function_with_warning():
    print('Перед генерацией предупреждения')
    warnings.warn('Это важное предупреждение', UserWarning)
    print('После генерации предупреждения')


for i in range(99, 102):
    b = 1 / i
    c = 1 / b
    if b < 0.01:

        warnings.simplefilter('error', UserWarning)
        function_with_warning()
        # print("\n")
        # print('риск деления на "0"', UserWarning)
    else:
        print('Программа нормально отрабатывает функцию при i =', i)

# # Пример 1: Фильтр установлен в "error"
# print("Пример 1: Фильтр 'default'", UserWarning)
# warnings.simplefilter('error', UserWarning)
# function_with_warning()

# # Пример 2: Фильтр установлен в "default"
# print("Пример 2: Фильтр 'default'")
# warnings.simplefilter('default', UserWarning)
# function_with_warning()
# print("\n")

# # Пример 3: Фильтр установлен в "ignore"
# print("Пример 3: Фильтр 'ignore'")
# warnings.simplefilter('ignore', UserWarning)
# function_with_warning()
#
# # Пример 4: Фильтр установлен в "always"
# print("Пример 4: Фильтр 'always'")
# warnings.simplefilter('always', UserWarning)
# function_with_warning()
