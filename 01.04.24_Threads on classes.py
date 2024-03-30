from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name, skill):
        super(Knight, self).__init__()
        self.name = name
        self.skill = skill

    def run(self, attack=100):
        for _ in range(1, attack + 1, self.skill):
            attack = attack - self.skill
            time.sleep(1)
            if attack <= 0:
                print(f' Рыцарь {self.name}: победа над врагами, умение: {self.skill}')
            else:
                print(f' Рыцарь {self.name} сражается')


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения
print('Рыцари начали сражаться.')
# print('Ждем когда Рыцари победят.')
knight1.start()
knight1.join()
knight2.start()
knight2.join()
