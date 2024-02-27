class Car:   # родительский(базовый) класс Car
    """Автомобили"""
    price = 1000000

    def horse_powers(self):
        horse_powers = 100
        return horse_powers

    def inspect(self):
        print('Стоимость автомобиля:', self.price)
        print('Мощность автомобиля:', self.horse_powers())


class Nissan(Car):
    """наследника класса Car - класс Nissan, переопределяет свойство price,
    а также переопределяет функцию horse_powers"""
    price = 1900000

    def horse_powers(self):
        horse_powers = 190
        return horse_powers


class Kia(Car):
    """наследника класса Car - класс Kia, переопределяет свойство price,
    а также переопределяет функцию horse_powers"""
    price = 1300000

    def horse_powers(self):
        horse_powers = 130
        return horse_powers


print('NISSAN:')
nissan = Nissan()
nissan.inspect()


print('KIA:')
kia = Kia()
kia.inspect()
