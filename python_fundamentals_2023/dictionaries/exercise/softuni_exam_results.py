submissions_by_language = {}
points_per_username = {}

while True:
    line = input()
    if line == "exam finished":
        break
    args = line.split('-')
    if args[1] == "banned":
        username = args[0]
        if username in points_per_username:
            points_per_username.pop(username)
    else:
        username = args[0]
        language = args[1]
        points = int(args[2])
        if language not in submissions_by_language:
            submissions_by_language[language] = []
            submissions_by_language[language].append(username)
        else:
            submissions_by_language[language].append(username)
        if username not in points_per_username:
            points_per_username[username] = points
        else:
            old_points = points_per_username[username]
            if points > old_points:
                points_per_username[username] = points
            else:
                continue
print("Results:")
for user, points in points_per_username.items():
    print(f"{user} | {points}")


print("Submissions:")
for programming_language, submissions in submissions_by_language.items():
    print(f"{programming_language} - {len(submissions)}")


