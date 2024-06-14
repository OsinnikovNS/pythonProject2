# Практическая работа по уроку "Динамическая типизация"
name = "Nikolay Osinnikov"
print("Имя:", name)
age = 51
print("Мой возраст:", age)
age = age + 1
print("Новый возраст:", age)
is_student = True
print("Студент:", is_student)

# проверка переменных на тип и вывод id
print("Тип переменной Имя:", type(name))
print("Является ли возраст целым числом:", isinstance(age, int))
print("Id переменной Имя:", id(name))
