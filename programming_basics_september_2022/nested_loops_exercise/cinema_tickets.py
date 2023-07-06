input_line = input()
ticket_total = 0
students_tickets = 0
standard_tickets = 0
kids_tickets = 0
while input_line != "Finish":
    available_tickets = int(input())
    ticket_counter = 0
    movie_command = input()
    while movie_command != "End":
        if movie_command == "standard":
            standard_tickets += 1
            ticket_counter += 1
        elif movie_command == "kid":
            kids_tickets += 1
            ticket_counter += 1
        elif movie_command == "student":
            students_tickets += 1
            ticket_counter += 1

        if ticket_counter == available_tickets:
            break
        movie_command = input()
    ticket_total += ticket_counter
    percentage = ticket_counter / available_tickets * 100
    print(f"{input_line} - {percentage:.2f}% full.")
    input_line = input()
print(f"Total tickets: {ticket_total}")
percentage_student_tickets = students_tickets / ticket_total * 100
percentage_standard_tickets = standard_tickets / ticket_total * 100
percentage_kid_tickets = kids_tickets / ticket_total * 100
print(f"{percentage_student_tickets:.2f}% student tickets.")
print(f"{percentage_standard_tickets:.2f}% standard tickets.")
print(f"{percentage_kid_tickets:.2f}% kids tickets.")
