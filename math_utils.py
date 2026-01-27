# creating custom py module with exception handling


def add(a, b):
    try:
        return a + b
    except TypeError:
        raise TypeError("Both inputs must be numbers")


def subtract(a, b):
    try:
        return a - b
    except TypeError:
        raise TypeError("Both inputs must be numbers")


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")
    except TypeError:
        raise TypeError("Both inputs must be numbers")

# print(add(a,b)) # check working or not