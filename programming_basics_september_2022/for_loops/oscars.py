actor_name = input()
academy_points = float(input())
num_of_graders = int(input())
final_grade = academy_points

for _ in range(1, num_of_graders + 1):
    current_grader = input()
    points = float(input())
    final_grade += (len(current_grader)*points)/2
    if final_grade >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {final_grade:.1f}!")
        break
diff = abs(1250.5 - final_grade)
if final_grade < 1250.5:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")

