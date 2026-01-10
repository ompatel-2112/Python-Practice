# List : Ordered and Mutable

"""
- List is mutable data type which is used when you have a collection of items
where the order matters and you might need to change the data later
- They allow duplicate members
"""
# Syntax: Defined with square brackets []

fruits = ["apple", "orange","banana"]

print(type(fruits))

# for access the elements - using index of element starts with 0th index
print(fruits[0])


# Tuples : Ordered and Immutable

"""
- Tuple is immutable data type(list
- we cannot use .append() or change an index in tuple
- Faster than lists; protects data from accidental change
"""

# Syntax: Defined with parentheses ()

tup = ('car', 'bus')
print((tup))
print(type(tup))


colour = ("red","green","pink")# use " " also
print(colour)

tup = tuple('Geeks')
print(tup)

#Creating a Tuple with Mixed Datatypes.

tup = (5, 'Welcome', 7, 'Geeks')
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Geeks',) * 3
print(tup1)


# Set : unorderd and unique

"""
- Sets are used when the uniqueness of items is the priority.They do not allow 
duplicate values
- Unindexed which we can not access elements using index
- No duplicates; very fast for "membership testing" (checking if an item exists).
- Math Logic: we can perform unions, intersections, and differences between two sets
""" 

# syntax: Defined with curly braces {}

box = {"pen","pencil","erazer","pen",  } #remove duplicate  automatically
basket = { 'fruit','vegitable','chocolet'} #also use ' '
print(box)
print(basket)
print(type(box))


# Dictionaries : key-value pairs 

"""
dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary
can be of any data type and can be duplicated, whereas keys can't be repeated and must be immutable.

Keys are case sensitive which means same name but different cases of Key will be treated distinctly.
Keys must be immutable which means keys can be strings, numbers or tuples but not lists.
Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
"""
# Syntax: {key: value}

user = {"name": "om patel", "age": 21}

print(user)
print(type(user))

print(user["name"])

print(user.get("name"))
