
"""
* What is a Function in Python?

A function is a block of reusable code that performs a specific task.

Instead of writing the same code again and again, we define it once and call it whenever needed

def key word is used for define function

"""

#example of function

def add(a, b):
    return a+b 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = add(a, b)
print(sum)

#Function with Parameters

def wel_msg(name):
    print("Good mornig", name)

x = input("Enter your name:")

wel_msg(x)

#nested function

# a function which have another function on it and we can use it only using outer function call

def outer():
    def inner():
        print("Inner function")
    inner()

outer()

# Recursive Function
# -> a function who calling its self

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))





