# подсчет суммы четных чисел в диапазоне от 2 до 999
s = 0
for i in range (2, 1000, 2):
    if i % 2 == 0:
        s +=i
print(s)
# Расчет суммы вводимых чисел"
s=0
n = int(input("Введите количество вводимых чисел "))
for i in range (n):
    i = int(input ())
    s+=i
print (s)
