# Создайте в директории проекта текстовый файл с расширением txt.
# Добавьте в этот файл текст.
# Создайте переменную с этим файлом.
# Распечатайте содержимое текстового файла в консоль.
# Закройте файл.

text = ["My soul is dark - Oh! quickly string\n",
        "The harp I yet can brook to hear;\n",
        "And let thy gentle fingers fling\n",
        "Its melting murmurs o'er mine ear.\n",
        "If in this heart a hope be dear,\n",
        "That sound shall charm it forth again:\n",
        "If in these eyes there lurk a tear,\n",
        "'Twill flow, and cease to burn my brain.\n",
        "\n",
        "But bid the strain be wild and deep,\n",
        "Nor let thy notes of joy be first:\n",
        "I tell thee, minstrel, I must weep,\n",
        "Or else this heavy heart will burst;\n",
        "For it hath been by sorrow nursed,\n",
        "And ached in sleepless silence, long;\n",
        "And now 'tis doomed to know the worst,\n",
        "And break at once - or yield to song.\n"]

f = open('text.txt', 'w')
f.writelines(text)
f.close()

f = open('text.txt', 'r')
file_content = f.read()
print(file_content)
f.close()

# Код для смены директории:
# new_directory = r"C:\pythonProject\pythonProject\pythonProject\Django_first_web\pythonProject3\send_e-mail_mes"os.chdir(new_directory)
# a = open('test.txt', 'w')
# print(os.getcwd())
# a.close()
# print(os.getcwd())
