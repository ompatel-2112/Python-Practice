#Even or odd checker

num = int(input("Enter the number:"))

if 2%num == 0 :
    print("number is even")

else : print ("number is odd")

#check number is positive/negative/ or zero

x= float(input("Enter num to check: "))

if x > 0:
    print("num is positive")

elif x < 0:
    print("num is negative")

else :
    print ("num is zero")

#multiplication table 

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n=int(input("enter the num for table:"))
multiplication_table(n)

#Find the Largest num in a list

def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_max([12, 45, 2, 89, 34])) # Output: 89

