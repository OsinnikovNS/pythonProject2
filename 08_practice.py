# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин,
# У человек есть степень сытости, немного еды и денег.
# Если сытость <0 единиц, человек умирает.
# Человеку надо прожить 365 дней
from random import randint
from termcolor import cprint


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return 'я - {}, сытость {}, еды осталось {}, денег осталось {}'.format(
            self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.food > 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        cprint('{} ходил на работу'.format(self.name), color='red')
        self.money += 50
        self.fullness -= 10

    def watch_tv(self):
        cprint('{} смотрел МТВ целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.money -= 50
            self.food += 50
        else:
            cprint('{} деньги закончились'.format(self.name), color='red')

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food <= 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_tv()


vasya = Man(name='Вася')
kolya = Man(name='Коля')
for day in range(1, 21):
    cprint('*************** день ******************'.format(day), color='blue')
    vasya.act()
    kolya.act()
    print(vasya)
    print(kolya)

# Создаем двух людей, живущих в одном доме - Васю и Колю
# Нужен класс Дом, в нем должен быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке

vasya = Man(name='Вася')
print(vasya)
vasya.eat()
print(vasya)
vasya.work()
print(vasya)
vasya.watch_tv()
print(vasya)
