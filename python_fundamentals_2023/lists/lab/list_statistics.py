n = int(input())
positive = []
negative = []
for _ in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
print(positive)
print(negative)
print(f"Count of positives is:{len(positive)}")
# sum_negative = 0
# for num in negative:
#    sum_negative = sum_negative + num
# print(f"Sum of negatives is: {sum_negative}")
print(f"Sum of negatives is: {sum(negative)}")

# extend() - gets the collection and adds to list
# append() - appends an element