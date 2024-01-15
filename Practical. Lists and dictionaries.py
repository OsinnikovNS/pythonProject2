# Практическое задание по теме: "Списки и словари"
my_list = []
my_list = ['apple', 'orange', 'watermelon', 'kiwi', 'banana', 'pear']
print('Список:', my_list)
print('первый элемент:', my_list[0])
print('последний элемент:', my_list[-1])
print('вывод элемента в списке с 3 по 5', my_list[3:6])
# замена третьего элемента в списке
del my_list[2]
my_list.insert(2,'lemon')
print('измененный список:', my_list)
# Работа со словарями
my_dict ={'яблоко': 'apple', 'апельсин': 'orange', 'лимон': 'lemon', 'киви': 'kiwi'}
print('Словарь:', my_dict)
# Вывод на экран значения для заданного ключа 'яблоко'.
print('Значение для ключа "яблоко":', my_dict['яблоко'])
# добавление дополнительного ключа - "арбуз"
my_dict.setdefault('арбуз', 'watermelon')
# Изменение значения для заданного ключа "лимон" на "мандарин"
my_dict['лимон'] = 'tangerine'
print('Измененный словарь:', my_dict)