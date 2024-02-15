"""Задача:
1. Создайте новый класс House.
2. Задайте ему новый атрибут numberOfFloors = 10
3. В цикле пройдитесь по атрибуту numberOfFloors и распечатайте значение
"Текущий этаж равен" Полученный код напишите в ответ к домашнему заданию"""


class House:
    def __init__(self):
        self.number_of_floors = 10


House1 = House()
print('Всего этажей: ', House1.number_of_floors)

for i in range(0, House1.number_of_floors):
    print('Текущий этаж равен', i + 1)
