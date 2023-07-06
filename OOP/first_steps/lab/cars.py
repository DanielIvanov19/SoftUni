class Car:
    def __init__(self, name: str, model: str, engine: str):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


toyota = Car("Toyota", "Camri", "2.0")
print(toyota.name, toyota.model, toyota.engine)
print(toyota.get_info())