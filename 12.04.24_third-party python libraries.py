# 1. Выберите одну или несколько сторонних библиотек Python, например, requests.
# Изучите документацию выбранной библиотеки, ознакомиться с основными возможностями и функциями.
# Напишите простые задачи, в которых нужно использовать выбранные библиотеки, и выполните их.
# Приведите примеры использования библиотек в различных сценариях:
#  - Запросить данные с помощью библиотеки requests из API и вывести их в консоль.
# Поясните, как выбранные библиотеки помогли в решении поставленных задач и какие преимущества
# они предоставили по сравнению с базовым функционалом Python.
# ------------------------------------------------------------------------------
import requests

api_key = 'e92c5026eb2a466eb09e1591f5ee035f'

city = input('Введите город (например Moscow): ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    visibility = data['visibility']
    desc = data['weather'][0]['description']

    print(f'Температура: {temp} C')
    print(f'Давление: {pressure} мм')
    print(f'Влажность: {humidity} %')
    print(f'Видимость: {visibility} м')
    print(f'Описание: {desc}')
else:
    print('Ошибка при получении данных о погоде')
