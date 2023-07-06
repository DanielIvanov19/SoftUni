class Mammal:
    __kingdom = 'animals'
    def __init__(self, name: str, type: str, sound: str):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f'{self.name} is of type {self.type}'

m = Mammal('Dog', 'Domestic', 'Bark')
m2 = Mammal('Cat', 'Domestic', 'Meow')
m3 = Mammal('Cat2', 'Domestic', 'Meow')

print(m2.get_kingdom())
print(m.info())
print(m.get_kingdom())
print(m3.get_kingdom())