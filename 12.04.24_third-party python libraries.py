# 1. Выберите одну или несколько сторонних библиотек Python, например, requests.
# Изучите документацию выбранной библиотеки, ознакомиться с основными возможностями и функциями.
# Напишите простые задачи, в которых нужно использовать выбранные библиотеки, и выполните их.
# Приведите примеры использования библиотек в различных сценариях:
#  - Запросить данные с помощью библиотеки requests из API и вывести их в консоль.
# Поясните, как выбранные библиотеки помогли в решении поставленных задач и какие преимущества
# они предоставили по сравнению с базовым функционалом Python.
# ------------------------------------------------------------------------------
from api_key import API_KEY
import requests
from datetime import datetime as dt

# для возможности ввода наименования города с клавиатуры
# city = input('Введите город (например Moscow): ')
# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key} - вывод по широте и долготе.
spisok = (
            'Yekaterinburg',
            '     Perm    ',
            '    Kazan    ',
            '  Berezniki  ',
            'Krasnovishersk'
        )
for i in range(len(spisok)):
    city = spisok[i]
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
    print(f'********************* {city} ***********************')
    response = requests.get(url)
    print(f'Погода в {city} на дату: {dt.now().strftime('%d %b %G %H:%M:%S')}')
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        clouds = data['clouds']['all']
        # precipitation = data['main']['precipitation']
        visibility = data['visibility']
        pressure = data['main']['pressure']
        desc = data['weather'][0]['description']

        print(f'Температура: {temp} °C')
        print(f'Скорость ветра: {wind_speed} м/с')
        print(f'Влажность: {humidity} %')
        print(f'Облачность: {clouds} %')
        # print(f'Осадки: {precipitation} мм/ч')
        print(f'Видимость: {visibility} м')
        print(f'Давление: {pressure} мм')
        # print(f'Описание: {desc}')
    else:
        print('Ошибка при получении данных о погоде')
