#number = int(input())

#number_to_string = str(number)
#number_length = len(number_to_string)
#number_to_string.split("")
#s = [number_to_string]
#print(number_to_string)

number = int(input())
mylist = list(map(int, str(number)))
mylist.sort(reverse=True)
generated_number = mylist[0]

for i in range(1, len(mylist)):
    generated_number = generated_number * 10 + mylist[i]
print(generated_number)

