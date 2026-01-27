import math_utils

a = int(input("enter the a :"))
b = int(input("enter the b :"))

try:
    print("Addition:", math_utils.add(a,b))
    print("Subtraction:", math_utils.subtract(a,b))
    print("Division:", math_utils.divide(a,b))  # error case

except Exception as e:
    print("Error:", e)
