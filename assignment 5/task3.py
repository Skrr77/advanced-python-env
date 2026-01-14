class Person:
    def __init__(self, name):
        self._name = name  # encapsulation

    def get_info(self):
        return f"Person name: {self._name}"


class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def get_info(self):  # polymorphism
        return f"Student name: {self._name}, Major: {self.major}"


person = Person("John")
student = Student("Anna", "Computer Science")

print(person.get_info())
print(student.get_info())
