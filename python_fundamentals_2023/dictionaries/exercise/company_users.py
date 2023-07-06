employees_company = {}

while True:
    line = input()
    if line == "End":
        break

    args = line.split(" -> ")
    company_name = args[0]
    employee_id = args[1]

    if company_name not in employees_company:
        employees_company[company_name] = []

    if employee_id not in employees_company[company_name]:
        employees_company[company_name].append(employee_id)


for company, employees in employees_company.items():
    print(company)
    for employee in employees:
        print(f'-- {employee}')
        