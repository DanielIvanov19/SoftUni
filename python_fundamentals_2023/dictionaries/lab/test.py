translations = {"cat": "tiger", "dog": "corgi", "красив": ["beautiful", "pretty", "nice looking"]}

# print(translations["cat"])
# .get(key, exception)
# print(translations.get("Cat", "No such key"))
# add values
translations["cat"] = "new value"
# print(translations["cat"])
translations["прасе"] = "pig"

school = {"1a": ["Annie", "Bob", "Karina"], "1b": ["Valerie", "Boris", "Vlada"]}

# nums

nums = {1: "one", 2: "two", 3: "three"}

# for key in nums:
# print(key, nums[key])
# print(nums.items())
# items() -> returns tuple(key, value)

searched_value = "two"
for key, value in nums.items():
    if value == searched_value:
        print(key)

for value in nums.values():
    if value == searched_value:
        print("presented in that dict")

# pop() -> returns the value and removes the element with the specified key
# popitem() -> removes an item that was last inserted, returns the key and the value
# del nums[key]

students_2 = {1: {'name': 'Peter', 'age': 22}}
