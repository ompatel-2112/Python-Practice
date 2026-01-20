# Python Modules

"""
what is module?
Consider a module to be the same as a code library.

A module in Python is simply a file that contains Python code (functions, variables, classes, or runnable code).
Its purpose is to organize code, reuse code, and keep programs clean and manageable

A file containing a set of functions you want to include in your application.

"""
# create a module
# -> To create a module just save the code you want in a file with the file extension
# ex - Save this code in a file named mymodule.py

"""def greeting(name):
     print("Hello, " + name)

 """
# use a module
# we can use the module we just created, by using the import statement

"""
 Ex : 

import mymodule

mymodule.greeting("Jonathan") """

import mymodule

mymodule.greeting("hari")

#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)

import mymodule

a = mymodule.person1["age"]
print(a)

# naming a module
# - we can name the module file whatever you like, but it must have the file extension .py

# Re-naming a module
"""
we can create an alias when you import a module, by using the as keyword:

import mymodule as mm

x = mm.person1["city"]
print(x)


"""
import mymodule as mm

x = mm.person1["city"]
print(x)

""" 
Built-in Modules :
There are several built-in modules in Python, which you can import whenever you like.
Ex  - math

    - random

    - datetime
"""
# math

import math

print(math.sqrt(25))      # Square root
print(math.pow(2, 3))     # Power
print(math.factorial(5))  # Factorial


# random 

import random

print(random.randint(1, 10))   # Random number between 1 and 10

print(random.choice([10, 20, 30, 40]))  # chose random num

# datetime Module

import datetime

today = datetime.date.today()
print(today) 
