class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


student = Student('Alice', 20, '1234')
print(student.name)
print(student.age)
print(student.student_id)
