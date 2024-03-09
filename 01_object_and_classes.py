# Описываем одинаковые объекты одним классом
class VAZ():
    def __init__(self):
        self.color = 'синий металлик'
        self.price = '1 700 000 руб'
        self.max_velocity = '180 км/ч'
        self.current_velocity = '0 км/ч'
        self.engin_rpm = 0

    def start(self):
        print('Мотор запущен')
        self.engine_rpm = 700

    def go(self):
        print('Поехали')
        self.engine_rpm = 2000
        self.current_velocity = '20 км/ч'


# my_car = VAZ
# # объекты имеют свойства, к которым можно обратиться с помощью точки
# print(my_car.color)
# 'синий металлик'
# print(my_car.price)
# '1 700 000 руб'
# print(my_car.max_velocity)
# '180 км/ч'
# print(my_car.engine_rpm)
# 0
# print(my_car.current_velocity)
# '20 км/ч'

my_car = VAZ()
print(my_car)
print('цвет:', my_car.color)
print('цена:', my_car.price)
print('максимальная скорость:', my_car.max_velocity)

my_car.start()  # завести автомобиль
print('обороты:', my_car.engine_rpm)
my_car.go()   # начать движение
print('обороты:', my_car.engine_rpm)
print('установленная скорость:', my_car.current_velocity)

produced, plan = 0, 10
stock = []
while produced < plan:
    new_car = my_car
    stock.append(new_car)
    produced +=1
    print(stock)


