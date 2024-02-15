class House:
    def __init__(self):
        self.number = 0

    def number_of_floors(self, floors):
        """Количество этажей в доме"""
        self.number += floors


House1 = House()
for i in range(0, 10):
    House1.number_of_floors(1)
    print('Текущий этаж House1 равен:', House1.number)
