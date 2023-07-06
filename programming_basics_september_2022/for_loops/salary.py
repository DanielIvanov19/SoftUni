c_tabs = int(input())
init_salary = int(input())
salary = init_salary

for i in range(1, c_tabs + 1):
    name_tab = input()

    if name_tab == "Facebook":
        salary -= 150
    elif name_tab == "Instagram":
        salary -= 100
    elif name_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary")
else:
    print(salary)
