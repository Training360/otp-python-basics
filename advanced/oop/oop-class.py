print(type(10))


def user_factory(first_name, last_name, age):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    age = int(age)
    return first_name, last_name, age


class Student:
    __slots__ = ('first_name', 'last_name', 'age', 'subjects', '__neptun_code')

    school = 'Berklee'
    students = []

    def __init__(self, first_name, last_name, age, subjects, neptun_code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self._subjects = subjects
        self.__neptun_code = neptun_code
        Student.students.append(self)

    def print_fullname(self):
        print(f'{self.first_name} {self.last_name}')

    def avarage(self):
        return round(sum(i['grade'] for i in self.subjects) / len(self.subjects))

    def credits(self):
        return sum(i['credit'] for i in self.subjects if i['grade'] > 1)

    def print_neptun_code(self):
        print(self.__neptun_code)


print(Student.school)

student = Student('John', 'Doe', 33, [
    {'subject': 'mathematics', 'credit': 4, 'grade': 3},
    {'subject': 'physics', 'credit': 3, 'grade': 1},
    {'subject': 'algorithms', 'credit': 5, 'grade': 4}
], 'JDA012')
print(type(student))
print(student)
print(student.first_name)
print(student.last_name)
print(student.age)
student.print_fullname()
print(student.avarage())

# student.pet = 'cat'
# print(student.pet)

student_2 = Student('jane', 'Doe', 30, [
    {'subject': 'mathematics', 'credit': 4, 'grade': 2},
    {'subject': 'physics', 'credit': 3, 'grade': 5},
    {'subject': 'algorithms', 'credit': 5, 'grade': 5}
], 'JJJ123')

print(student_2.credits())
student_2.age = 20
print(student_2.age)
print(student.school)

Student.school = 'SZE'
print(Student.school)
print(student.school)
print(student_2.school)
print(Student.students)
print([i.first_name for i in Student.students])
# print(student.__neptun_code)
student.print_neptun_code()

print(student._Student__neptun_code)
