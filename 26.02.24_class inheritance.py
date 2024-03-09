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

# ---------------------------------------------------------------

# class Vehicle:
#     def __init__(self, make, model, year, price):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price
#
#     def display_info(self):
#         print(f"Марка: {self.make}"
#         f"\nМодель: {self.model}"
#         f"\nГод выпуска: {self.year}"
#         f"\nСтоимость: {self.price} руб")
#
# class Car(Vehicle):
#     def __init__(self, make, model, year, price, num_doors, body_style):
#         super().__init__(make, model, year, price)
#         self.num_doors = num_doors
#         self.body_style = body_style
#
#
# class Truck(Vehicle):
#     def __init__(self, make, model, year, price, bed_length, towing_capacity):
#         super().__init__(make, model, year, price)
#         self.bed_length = bed_length
#         self.towing_capacity = towing_capacity
# # создаем объект "легковой автомобиль"
# car = Car("Toyota", "Camry", 2022, 2900000, 4, "седан")
#
# # создаем объект "грузовик"
# truck = Truck("Ford", "F-MAX", 2023, 6000000, "6162", "13 т")
#
# # выводим информацию о легковом автомобиле и грузовике
# car.display_info()
# truck.display_info()
