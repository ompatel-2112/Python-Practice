"""
-> set -
A set is an unordered collection of unique elements. created using { }

"""

# Creating a Set
set1 = {1, 2, 3}

print(type(set1))



# Empty set must be created using:

empty_set = set()


# operation on set

# Adding Elements
# add() – Add single element
s = {1, 2, 3}

s.add(4)
s.add(8) # add elemant on last index 
print(s)


# update() – Add multiple elements

s.update({5, 6, 7})
print(s)

# Removing Elements

# remove() – Removes element (error if not found)
s.remove(3)

# discard() – No error if element not found
s.discard(10)

# pop() – Removes random element
s.pop()

# clear() – Removes all elements
s.clear()

# Membership Test (in keyword) show  that elemant present on set or not 
# ->Very fast compared to list search

s2 = {10, 20, 30}

print(20 in s2)   # True
print(40 in s2)   # False



# Set Union ( | or union() )

# Combines elements from both sets (no duplicates).

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
print(A.union(B)) # 1 2 3 4 5

# Set Intersection ( & or intersection() )

# Common elements in both sets.

print(A & B)
print(A.intersection(B)) # 3


# Set Difference ( - or difference() )
# Elements present in A but not in B.

print(A - B)
print(A.difference(B)) # 1 2


# Symmetric Difference ( ^ or symmetric_difference() )
#Elements present in either set but not both.

print(A ^ B)
print(A.symmetric_difference(B))  # 1 2 4 5


# Subset & Superset
# issubset()
A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))  # True

# issuperset()
print(B.issuperset(A))  # True

# Disjoint Sets

# No common elements use for check if set consist of any common elements on them 

A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))  # True

# Copying a Set
new_set = A.copy()

# Length of Set
print(len(A))
