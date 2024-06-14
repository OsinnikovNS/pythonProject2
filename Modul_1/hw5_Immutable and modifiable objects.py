# Практическая работа по теме "Неизменяемые и изменяемые объекты. Кортежи"
mutable_list = []
mutable_list = [1,5,3,4,2]
print('Список', mutable_list)
mutable_list.append('добавление в список')
# расширение списка
print('- добавление в список:', mutable_list)
mutable_list.extend([30, 10, 11])
print('- расширение списка цифрами 30,10 и 11:', mutable_list)
del mutable_list[5]
print('- удаляем 5 элемент в строке', mutable_list)
print('- минимальный элемент в строке:', min (mutable_list))
print('- максимальный элемент в строке:', max (mutable_list))
mutable_list.sort()
print('- сортировка строки: ', mutable_list)
# Кортеж
immutable_var = tuple[2,3,'f','student', 10]
print('- кортеж:', immutable_var)

