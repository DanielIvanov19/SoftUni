def gather_credits(required_credits, *courses):
    enrolled_courses = set()
    gathered_credits = 0

    for course, credits_from_course in courses:
        if gathered_credits >= required_credits:
            break

        if course not in enrolled_courses:
            enrolled_courses.add(course)
            gathered_credits += credits_from_course

    if gathered_credits >= required_credits:
        sorted_courses = sorted(enrolled_courses)
        courses_str = ", ".join(sorted_courses)
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {courses_str}"
    else:
        credits_shortage = required_credits - gathered_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

