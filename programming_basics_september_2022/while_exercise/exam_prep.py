poor_grades = int(input())
flag = False
last_problem = ""
grades_sum = 0
grades_count = 0
curr_poor = 0
input_line = input()

while input_line != "Enough":
    problem_name = input_line
    current_grade = int(input())
    if current_grade <= 4:
        curr_poor += 1

    if curr_poor >= poor_grades:
        flag = True
        break
    grades_sum += current_grade
    grades_count += 1
    last_problem = problem_name
    input_line = input()

if flag:
    print(f"You need a break, {curr_poor} poor grades.")
else:

    average = grades_sum / grades_count
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {grades_count}")
    print(f"Last problem: {last_problem}")