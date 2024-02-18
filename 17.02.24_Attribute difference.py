""" Задача:
1. Создайте новый класс Buiding с атрибутом total
2. Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных
объектов класса Building total (по примеру класса Lemming из урока)
3. В цикле создайте 40 объектов класса Building и выведите их на экран командой print"""

from random import random, randint

class Building:
    total = 0

    def __init__(self):
        Building.total += 1


quantity = []
quantity_size = randint(1, 40)
while len(quantity) < quantity_size:
    new_building = Building()
    quantity.append(new_building)
print(Building.total)


