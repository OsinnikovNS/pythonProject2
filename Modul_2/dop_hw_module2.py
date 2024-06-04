from random import randint


def trap(n):
    unique = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                unique += str(i) + str(j)
    return f'{n} - {unique}\nПоздравляю вас не раздавят, сокровище на верхней полке'


#  way 1
# n = randint(3, 20)
# print('Рандом решит твою судьбу')

#  way 2
n = int(input("Привет Indiana J. введи число и если оно будет кратно сумме каждой пары то вы будете жить ;): "))

indiana_jones = trap(n)
print(indiana_jones)