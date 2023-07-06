init_schedule = input().split(', ')

user_input = input()
while user_input != 'course start':
    command = user_input.split(':')[0]
    lesson_title = user_input.split(':')[1]
    if command == 'Add':
        if lesson_title not in init_schedule:
            init_schedule.append(lesson_title)
    if command == 'Insert':
        index = int(user_input.split(':')[2])
        if lesson_title not in init_schedule:
            init_schedule.insert(index, lesson_title)
    if command == 'Remove':
        if lesson_title in init_schedule:
            init_schedule.remove(lesson_title)
        exercise = f'{lesson_title}-Exercise'
        if exercise in init_schedule:
            init_schedule.remove(exercise)
    if command == 'Swap':
        lesson_title_2 = user_input.split(':')[2]
        if lesson_title in init_schedule and lesson_title_2 in init_schedule:
            index_of_first = init_schedule.index(lesson_title)
            index_of_second = init_schedule.index(lesson_title_2)
            init_schedule[index_of_first], init_schedule[index_of_second] = init_schedule[index_of_second], init_schedule[index_of_first]
            exercise = f'{lesson_title_2}-Exercise'
            if exercise in init_schedule:
                init_schedule.remove(exercise)
                init_schedule.insert(index_of_first + 1, exercise)
    if command == 'Exercise':
        exercise = f'{lesson_title}-Exercise'
        if lesson_title not in init_schedule:
            init_schedule.append(lesson_title)
            init_schedule.append(exercise)
        elif lesson_title in init_schedule:
            if exercise in init_schedule:
                continue
            else:
                index_of_lesson = init_schedule.index(lesson_title)
                init_schedule.insert(index_of_lesson + 1, exercise)
    user_input = input()

for lesson in init_schedule:
    print(f'{init_schedule.index(lesson) + 1}.{lesson}')