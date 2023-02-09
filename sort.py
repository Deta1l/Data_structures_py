a = [1, 233, 43, 54, 54, 4, 76]
a1 = [1, 233, 43, 54, 54, 4, 76, 'aa', 'asas']
b = {1: 'D', 3: 'B', 2: 'B', 4: 'E', 5: 'A'}
a.sort()
b = sorted(b)
print(a,a1,b)

print(sorted("This is a test string from Andrew ta".split(), key=str.lower))



student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2]))   # сортируем по возрасту


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
    def weighted_grade(self):
        return 'CBA'.index(self.grade) / self.age

student_objects = [
    Student('dave', 'G', 15),
    Student('jane', 'B', 12),
    Student('jane', 'A', 10),
]
print(sorted(student_objects, key=lambda student: student.grade, reverse=True))