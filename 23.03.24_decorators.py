"""Напишите 2 функции:
Функция которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат
 1ой функции будет простым числом и "Составное" в противном случае."""

def sum_three(a, b, c):
    res = a + b + c
    return res


def is_prime():
    def wrapper():
        res = sum_three()
        for i in range(2, res // 2 + 1):
            if res % i == 0:
                k = k + 1
        if (k <= 0):
            print("Число простое")
        else:
            print("Число не является простым")


result = sum_three(2, 3, 6)
print(result)




