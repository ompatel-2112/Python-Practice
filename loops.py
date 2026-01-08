#python mainly has two types of loops 

"""
1.for loop
  When you know in advance how many times you want to repeat something

2.while loop
  When you do not know how many times the loop will run depends on a condition
"""

"""
* syntax of for loop

for variable in (sequence):
    statement

ex. 

for i in range(1,6):
        print(i)

output: 1
        2
        3
        4
        5
"""
for i in range(1,6):
        print(i)

#print each character of a string 

name = "om patel"
for ch in name:
    print(ch)

#Sum of numbers from 1 to 10

total = 0
for i in range(1, 11):
    total += i
print("Sum =", total)

"""
*syntax of while loop

 while condition:
    statement

ex.

i = 1
while i <= 5:
    print(i)
    i += 1

"""
i = 1
while i <= 5:
    print(i)
    i += 1

#print each character of a string

nam = "ravi"
index = 0
while index<=3:
     print(nam)
     index += 1


