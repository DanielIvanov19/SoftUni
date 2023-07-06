class Vehicle:
    def __init__(self, mileage: float, max_speed: int = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


    def __repr__(self):
        return f'This is {self.max_speed} {self.mileage}'

car = Vehicle(20)
print(car.max_speed)


