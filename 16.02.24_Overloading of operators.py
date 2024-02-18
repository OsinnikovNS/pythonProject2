"""Задача:
1. Создайте новый класс Building
2. Создайте инициализатор для класса Building, который будет задавать целочисленный
атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
3. Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType
для сравнения"""


class Building:
    """Здание"""

    # задаем целочисленный атрибут этажности и строковый атрибут
    def __init__(self, numberOfFloors=10, buildingType='газобетон'):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
        print(self.numberOfFloors, 'этажей,')
        print('материал', self.buildingType)

    def __eq__(self, other):  # переопределяем атрибуты
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

building_1 = Building(5, 'кирпич')
building_2 = Building(5, 'кирпич')
building_3 = Building()
if building_1 == building_2 == building_3:
    print('Здания одинаковые')
else:
    print('Здания различные')
