book_pages = int(input())
pages_per_hour = int(input())
deadline = int(input())
hours_per_day = book_pages//pages_per_hour//deadline
print(hours_per_day)