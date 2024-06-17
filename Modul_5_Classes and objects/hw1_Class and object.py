
# https://www.yandex.ru/video/preview/7091423872646590854

class House:
    """Описание дома"""
    def __init__(self, street, number):
        """Свойства дома"""
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """Строим дом"""
        print('Дом на улице ' + self.street + ' под номером ' + str(self.number) + ' построен.')

    def age_of_house(self, year):
        """Возраст дома"""
        self.age += year


House1 = House('ул. Московская', 20)
House2 = House('ул. Московская', 21)


print(House1.street, House1.number)
print(House2.street, House2.number)
House1.build()
House1.age_of_house(5)
print(House1.age)


class ProspectHouse(House):
    """Дома на проспекте"""
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect


PrHouse = ProspectHouse('пр. Ленина', 5)

print(PrHouse.prospect, PrHouse.number)
