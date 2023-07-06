n = int(input())


def get_average_grades(grades):
    return sum(grades) / len(grades)


grades_student = {}

for _ in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in grades_student:
        grades_student[student_name] = []

    grades_student[student_name].append(student_grade)

# average_grade_student = {student: get_average_grades(grades) for student, grades in grades_student.items() if
# get_average_grades(grades) >= 4.5}
# dictionary comprehension -> elegant solution

for student, grades in grades_student.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")
#print(average_grade_student)
