import math


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector2D(-self.x, -self.y)


x = Vector2D(3, 4)

Vector2D(3, 4)
print(x)


# class A:
#     def __init__(self, name, age, growth, weight):
#         self.name = name
#         self.age = age
#         self.growth = growth
#         self.weight = weight
#
#
# a = A('Вася', 99, 165, 78)
#
# print('Имя:', a.name, 'Возраст:', a.age, 'Вес:', a.weight, 'Рост:', a.growth)

# def test2(x, y, z):
#     return (x*2+y*2+z*2)
#
# res = test2(2,3,4)
# print('Результат:', res)

# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')
# name = input()
# # print('Java')
# # print('Ruby')
# # print('Scala')
# print('Python', end='+')  # print('C++')
# # print('GO')
# print('C#', end='=')  # print('C')
# print('awesome')
# # finish

# num = int(input())
# d3 = num % 10
# d2 = (num // 10) % 10
# d1 = num // 100
# print(d1, d2, d3, sep='')
# print(d1, d3, d2, sep='')
# print(d2, d1, d3, sep='')
# print(d2, d3, d1, sep='')
# print(d3, d1, d2, sep='')
# print(d3, d2, d1, sep='')


# for x in range(1, 11):
#     for y in range(x, 11):
#         if x*y == 2*x + 2*y + 4:
#             print(f'{x=}, {y=}')
# Программа Гвидо купил прямоугольную картину с рамкой.
# Форма картины и рамки укладывается ровно в клетчатую сетку,
# ширина рамки равна стороне 1 клетки. Оказалось, что площадь
# картины без рамки равна площади самой рамки.
# Какие размеры могут быть у картины с рамкой?
# a = 1
# while a <= 8:
#      b = 1
#      while b <= 10:
#          s1 = (a - 2) * (b - 2)
#          s2 = a*4
#          if s1 == s2:
#              print('Длинна сторон:', a, b)
#              print('Площадь:', s1, s2)
#          b += 1
#      a += 1

# Задача. На какую цифру оканчивается произведение всех простых
# чисел меньше миллиона?
# a = 0
# for i in range(10, 100):

#     if a = i % 2 != 0
#     elif:
#         a = i % 3 != 0
#     elif:
#         a = i % 5 != 0
#     print('число простое')
# else:
#     i+=1

# Листинг 1
# вводим N
# n = int(input("введите n: "))
# # создаем пустой список для хранения простых чисел
# lst = []
# # в k будем хранить количество делителей
# k = 0
# # пробегаем все числа от 2 до N
# for i in range(2, n + 1):
#     # пробегаем все числа от 2 до текущего
#     for j in range(2, i):
#         # ищем количество делителей
#         if i % j == 0:
#             k += k
#     # если делителей нет, добавляем число в список
#     if k == 0:
#         lst.append(i)
#     else:
#         k = 0
# # выводим на экран список
# print(lst)
# # перемножаем все числа в списке:
# import functools
# print(functools.reduce(lambda a, b: a * b, lst))
