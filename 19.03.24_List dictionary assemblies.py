def nam_2(x):
    return x**2


def add(x):
    return x % 2


my_number = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(nam_2, filter(add, my_number))
print(list(result))
