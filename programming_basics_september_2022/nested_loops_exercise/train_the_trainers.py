count_jury = int(input())

presentation = input()
sum_all_grades = 0
count_all_grades = 0
while presentation != 'Finish':
    sum_grades_per_presentation = 0
    for jury in range(1, count_jury + 1):
        grade = float(input())
        count_all_grades += 1
        sum_all_grades += grade
        sum_grades_per_presentation += grade
    average_grade_per_presentation = sum_grades_per_presentation / count_jury
    print(f"{presentation} - {average_grade_per_presentation:.2f}.")
    presentation = input()
print(f"Student's final assessment is: {sum_all_grades/count_all_grades:.2f}")
