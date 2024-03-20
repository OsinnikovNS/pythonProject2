"""Напишите класс-итератор EvenNumbers для перебора чётных чисел в
определённом числовом диапазоне. При создании и инициализации объекта
этого класса создаются атрибуты:
start – начальное значение (если значение не передано, то 0)
end – конечное значение (если значение не передано, то 1)"""


class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.step = 2

    def __iter__(self):
        self.value = self.start - self.step
        return

    def __next__(self):
        if self.value + self.step < self.end:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


en = EvenNumbers(10, 25)
for i in en:
    print(i)


# for i in range(10, 25):
#     if int(i) % 2 == 0:
#         print(i)
