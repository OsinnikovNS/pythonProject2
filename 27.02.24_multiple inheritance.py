# Множественное наследование (полиморфизм)
# class A:
#     def method_a(self):
#         print("Method A")
#
#
# class B:
#     def method_b(self):
#         print("Method B")
#
#
# class C(A, B):
#     pass
#
#
# c = C()
# c.method_a(), c.method_b()

# -------------------------------------------------------
class Vehicle:  # родительский(базовый) класс vehicle
    """Транспортное средство"""
    vehicle_type = "none"


class Car:  # родительский(базовый) класс Car
    """Автомобили"""
    price = 1000000

    def horse_powers(self):
        horse_powers = 100
        return horse_powers


class Nissan(Car, Vehicle):
    vehicle_type = "легковой"
    price = 1900000

    def horse_powers(self):
        horse_powers = 190
        return horse_powers

    def print_vehicle_type(self):
        print('Тип транспортного средства:', self.vehicle_type)
        print('Мощность двигателя:', self.horse_powers())
        print('Стоимость автомобиля:', self.price)


print('Автомобиль NISSAN')
my_car = Nissan()
my_car.print_vehicle_type()
