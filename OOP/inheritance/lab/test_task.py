class Person:
    def __init__(self, name, age):
        if not name:
            raise Exception('Person cannot be created without a name')
        if not age:
            raise Exception('Person cannot be created without age')
        self.name = name
        self.age = age

    def say_name(self):
        return f'Hello my name is {self.name}'

class Employee(Person):
    def __init__(self,name, age,  security_number):
        super().__init__(name, age)
        self.security_number = security_number


class Teacher(Employee):
    def __init__(self, name, age, security_number):
        super().__init__(name, age, security_number)

class Student(Person):
    pass  # this way it will use Person's init
s = Student('student', 22)
print(s)



p = Person('a', 55)
e = Employee('Blyat', 10, 25)
print(e.say_name())