"""Вариант 1 решения задачи"""
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name STR, age INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS grades (id INTEGER PRIMARY KEY, student_id, subject STR, grade FLOAT)")


class University:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect('students.db')
        self.cursor = self.conn.cursor()

    # Метод добавления студентов
    def add_student(self, name, age):
        self.cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    # Метод добавления оценок
    def add_grade(self, student_id, subject, grade):
        self.cursor.execute("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)",
                            (student_id, subject, grade))
        self.conn.commit()

    # Метод для возврата списка студентов
    def get_students(self, subject=None):
        if subject:
            self.cursor.execute("SELECT students.name, students.age, grades.subject, grades.grade FROM students "
                                "JOIN grades ON students.id = grades.student_id WHERE grades.subject = ?",
                                (subject,))
        else:
            self.cursor.execute("SELECT students.name, students.age, grades.subject, grades.grade FROM students JOIN "
                                "grades ON students.id = grades.student_id")
            self.conn.commit()
        students_data = self.cursor.fetchall()
        self.conn.commit()
        for row in students_data:
            if students_data:
                return students_data
            print(students_data)
            print(row)

        self.conn.commit()
        cursor.close()

    def __del__(self):
        self.conn.close()


u1 = University('Urban')

u1.add_student('Ivan', 26)  # id - 1
u1.add_student('Ilya', 24)  # id - 2
u1.add_student('Kolyan', 38)  # id - 3
u1.add_student('Vovan', 18)  # id - 4

u1.add_grade(1, 'Python', 4.8)
u1.add_grade(2, 'PHP', 4.3)
u1.add_grade(3, 'Python', 5)
u1.add_grade(4, 'Java', 4.1)

u1.add_grade(1, 'Python', 4.3)
u1.add_grade(2, 'PHP', 4.5)
u1.add_grade(3, 'Python', 4.9)
u1.add_grade(4, 'Java', 4.8)

print(u1.get_students())
print(u1.get_students('Python'))
