import math
students = int(input())
total_lectures = int(input())
additional_bonus = int(input())
students_presence = []
for student in range(1, students):
    presence = int(input())
    students_presence.append(presence)
max_presence = max(students_presence)
bonus = max_presence / total_lectures * (5 + additional_bonus)

print(f'Max Bonus: {math.ceil(bonus)}.')
print(f'The student has attended {max_presence} lectures.')