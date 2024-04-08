class Pet:
    """Домашние животные"""
    legs = 4
    has_tail = True

    def inspect(self):
        print('Всего ног:', self.legs)
        print('Хвост присутствует -', 'Да' if self.has_tail else 'нет')


def sound():
    print('Myau!')


class Cat(Pet):
    """Кот является домашним животным"""


class Dog(Pet):
    """Собака является домашним животным"""

    def sound(self):
        print('Gav!')


class Hamster(Pet):
    """Хомячок является домашним животным"""

    def sound(self):
        print('Ццццццццц!')

print('Котик:')
my_pet = Cat()
my_pet.inspect()
sound()

print('Собачка:')
my_pet = Dog()
my_pet.inspect()
my_pet.sound()

print('Хомячок:')
my_pet = Hamster()
my_pet.inspect()
my_pet.sound()

# pet = Pet(name='Кузя')
# print(pet.__class__ is Pet)