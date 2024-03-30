from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name, skill):
        super(Knight, self).__init__()
        self.name = name
        self.skill = skill

    def run(self, attack=100):
        print(f'{self.name},  на нас напали!')
        victory = int(attack / self.skill)
        for _ in range(1, attack + 1, self.skill):
            attack = attack - self.skill
            time.sleep(1)
            if attack <= 0:
                print(f' ********* Рыцарь {self.name} одержал победу спустя {victory} дней! *********')
            else:
                print(f' Рыцарь {self.name} сражается, осталось {attack} врагов.')


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения

knight1.start()
knight2.start()
knight1.join()
knight2.join()
