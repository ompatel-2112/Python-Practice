"""
A dictionary stores data in key-value pairs.

- Keys are unique
- Values can be any data type
- Dictionary is mutable

"""
student = {
    "name": "Om",
    "age": 21,
    "course": "Python"
}



# Creating a Dictionary

d1 = {"a": 1, "b": 2}
d2 = dict(name="Om", age=21)

print(d1)
print(d2)

print(type(d1))
print(type(d2))

# Empty dictionary

empty_dict = {}

# Accessing Values
# we use key for access element
print(student["name"])   # Om


# if key not found or present in dictionary than givs error

# Using get()

print(student.get("age"))
print(student.get("marks", "Not Available"))

# Adding Elements
# New key-value pair is added on dict

student["city"] = "Ahmedabad"

print(student)


# Updating Values
# Existing value gets updated

student["age"] = 22



# Removing Elements

# pop() - Remove by key

student.pop("course")

# popitem() - Remove last inserted item

student.popitem()

# clear() – Remove all items

# student.clear()


# Checking Key Existence

print("name" in student)   # true
print("marks" in student)  # false

# Dictionary Keys, Values & Items

print(student.keys())  #dict_keys(['name', 'age'])
print(student.values())  #dict_values(['Om', 22])
print(student.items())  #dict_items([('name', 'Om'), ('age', 22)])



# Looping Through Dictionary
# Loop through keys

for key in student:
    print(key, student[key])

# Loop through values

for value in student.values():
    print(value)


# Dictionary Length

print(len(student))

# Copying a Dictionary :

# using copy()

new_dict = student.copy()

# using dict()
# new_dict = student creates reference, not copy 

new_dict = dict(student)



# Updating Multiple Items
student.update({"age": 23, "marks": 85})

# Nested Dictionary

students = {
    1: {"name": "Om", "age": 21},
    2: {"name": "Raj", "age": 22}
}

print(students[1]["name"])

# advance operation

# Dictionary Comprehension 

squares = {x: x*x for x in range(1, 6)}
print(squares)


# Built-in Functions

count = {"boys": 80, "girls": 67}

print(max(count))   # boys (max key)
print(min(count))   # girls
print(sum(count.values()))  #147
