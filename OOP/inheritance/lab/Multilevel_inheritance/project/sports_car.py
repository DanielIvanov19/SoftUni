from project.car import Car

class Sports_Car(Car):
    def race(self):
        return 'racing...'

sc = Sports_Car()
print(sc.move())