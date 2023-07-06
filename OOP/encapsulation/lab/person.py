class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age  # age is the name of the method, NOT A PROPERTY NAME

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value <= 0:
            raise Exception("Age must be greater than zero")
        self.__age = value

person = Person('Kolio', 35)
person.age = 25