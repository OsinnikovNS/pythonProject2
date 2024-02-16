"""Задача:
1. Создайте новый класс House.
2. Создайте инициализатор для класса House, который будет задавать атрибут
этажности self.numberOfFloors = 0
3. Создайте метод setNewNumberOfFloors(floors), который будет изменять
атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors"""


class House:
    def __init__(self):
        self.number_of_floors = [0]

    def setNewNumberOfFloors(self, floors):
        """Метод, который изменяет атрибут numberOfFloors на параметр floors
        и выводить в консоль numberOfFloors"""
        self.number_of_floors.append(floors)
        print(self.number_of_floors)

    def inspect(self):
        """Проверка этажей"""
        for floors in self.number_of_floors:
            print('этажей', floors)


my_house = House()
my_house.setNewNumberOfFloors(floors=5)
my_house.inspect()
