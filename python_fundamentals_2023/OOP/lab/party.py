class Party:
    def __init__(self):
        self.people = []


p1 = Party()
p2 = Party()
print(p1.people)
print(p2.people)

people = []
name = input()
while name != "End":
    people.append(name)
    name = input()

