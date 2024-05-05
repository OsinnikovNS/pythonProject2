from main import Student
from unittest import TestCase
import unittest


class TestStudent(unittest.TestCase):
    """Метод - тест от метода run - бег на дистанцию 10 раз по 10 м"""

    def test_run(self):
        student1 = Student('Vovan')
        for _ in range(10):
            student1.run()
            """тестируем с дистанцией 1000 м"""
        self.assertEqual(student1.distance, 1000,
                             f'Дистанции не равны [дистанция студента {student1.name}] != 1000')

    """Метод - тест от метода walk - пеший ход на дистанцию 10 раз по 5 м"""

    def test_walk(self):
        student2 = Student('Kolyan')
        for _ in range(10):
            student2.walk()
            """тестируем с дистанцией 500 м"""
        self.assertEqual(student2.distance, 500,
                             f'Дистанции не равны [дистанция студента {student2.name}] != 500')

    """Тест на проверку дистанции (человек бегущий > человек идущий)"""

    def test_Greater(self):
        student1 = Student('Vovan')
        student2 = Student('Kolyan')
        for _ in range(10):
            student1.run()
            res1 = student1.distance
            student2.walk()
            res2 = student2.distance
        self.assertGreater(res1, res2,
                               f'Идущий {student2.name} должен преодолеть дистанцию меньше, чем бегущий {student1.name}')

    """Тест на проверку дистанции (человек бегущий < человек идущий)"""

    def test_Less(self):
        student1 = Student('Vovan')
        student2 = Student('Kolyan')
        for _ in range(100):
            student1.run()
            student2.walk()
        self.assertLess(student1.distance, student2.distance,
                            f'Бегущий {student1.name} должен преодолеть дистанцию больше, чем идущий {student2.name}')


if __name__ == '__main__':
    #     запускаем автодискавер тестов
    unittest = main()
