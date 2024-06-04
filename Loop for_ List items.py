# Домашняя работа по уроку "Цикл for. Элементы списка.
# Полезные функции в цикле"
cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for car in cars:
    print('Я езжу на автомобиле марки:', car)
cars_count = 0
for i in range(0, 11, 2):
    cars_count += 10
    print(cars_count, end=' ')
# end=' '- вывод данных для печати в одну строку через пробел
# для печати с новой строки используем команду print(end='\n') - (перевод на новую строку)
print('Конец подсчета.')
print(end='\n'), print(end='\n')
print('Конец подсчета.')

print(end='\n'), print(end='\n')
print('Второе решение задачи:')
cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for car in cars:
    cars_count += 10
    print('Я езжу на автомобиле марки:', car)
    print(cars_count)
