class Person:
    def __init__(self, name):
        self.name = name
        self.__security_number = '123456'  # _... ->protected -> visible in the class and in its inheritance
                                          # __... -> private -> visible only in the class
    def some_method(self):
        return 'Hi'

    # way for setting up getters and setters
    def get_security_number(self):
        return self.__security_number[-1]

    def set_security_number(self, new_value):
        today = '2023-29-06'
        if today > '2024-01-01':
            self.__security_number = new_value

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self._security_number = 'S' + self._security_number
    def say_hi(self):
        return 'Hi'

p = Person('Test')
# print(p._Person__security_number) syntax for __ 
print(p._security_number)  # syntax for _



