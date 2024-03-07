#  "Файлы в операционной системе".
import os
import time

directory = 'D:/Temp/Books Python'  # Указать путь к вашему каталогу

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f"Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, "
              f"Время изменения: {formatted_time}, Родительская директория: {parent_dir}")
print(os.walk(directory))
print("Текущая директория:", os.getcwd())  # напечатать наименование текущей директории

