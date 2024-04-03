# TODO Напишите 2 функции:
# TODO 1. Функцию, которая складывает 3 числа (sum_three);
# TODO 2. Функцию декоратор (is_prime), которая распечатывает "Простое", если результат
#  1ой функции будет простым числом и "Составное" в противном случае.


def is_prime(func):  # Функция декоратор
    def wrapper(*args):
        k = 0
        for i in range(2, sum(args) // 2 + 1):
            if sum(args) % i == 0:
                k = k + 1
        if k <= 0:
            print("Простое")
        else:
            print("Составное")
        print(sum(args))

    return wrapper


# @is_prime
def sum_three(*args):
    print(sum(args))
    return

print('Без декоратора функция sum_three:')
sum_three(1, 3, 6)
print('С декоратором is_prime, функция sum_three:')
decorator = is_prime(sum_three)
decorator(2, 3, 6)
