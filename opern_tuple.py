# Creating a Tuple
t1 = (10, 20, 30)
t2 = 10, 20, 30   # without parentheses
t3 = (10,)        # single-element tuple (comma is required)

# Accessing Elements using ndexing
t = (5, 10, 15, 20)

print(t[0])    # 5
print(t[-1])   # 20

# Slicing

tup = (1, 2, 3, 4, 5)

print(tup[1:4])   # (2, 3, 4)
print(tup[:3])    # (1, 2, 3)
print(tup[::2])   # (1, 3, 5)

# Concatenation - combining 2 tuple using +

# Combine two tuples:

tup1 = (1, 2)
tup2 = (3, 4)

tup3 = tup1 + tup2
print(t3)   # (1, 2, 3, 4)

# Repetition - using *

# Repeat tuple elements:

tupl = (1, 2)
print(tupl * 3)   # (1, 2, 1, 2, 1, 2)

# embership Test (in, not in)
tup_1 = (10, 20, 30)

print(20 in tup_1)      # True
print(50 not in tup_1)  # True

# Length of Tuple (len)

tuPl = (1, 2, 3, 4)
print(len(tuPl))   # 4

# Iterating Through Tuple
# Using for loop

t = (10, 20, 30)

for i in t:
    print(i)