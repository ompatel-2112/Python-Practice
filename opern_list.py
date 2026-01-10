# creating list - []

num = [ 10,12,14,16,18]
name = ["om","ravi","harsh","nita"]
mix = [20, " riya",17, " dixit" , True , 4.5]

# Accessing Elements - using index [0]

marks = [ 70,98,84,69]

print(marks[0])   # 70
print(marks[2])   # 84
print(marks[3])   # 69
print(marks[-1])  # 69 (last element)

#Slicing a list - [starting index : ending index + 1(exclusive)]

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30] [ initialy 0  index : last indx + 1]
print(numbers[2:])    # [30, 40, 50] [ start index : initialy last index]

#Adding Elements : append() – Add one element at end

numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

#insert() – Add at specific position
numbr = [1 , 2 , 3 ,4]
numbr.insert(1, 50) # [1, 50, 2, 3, 4]
print(numbr)

#extend() – Add multiple elements


numbr.extend([5,6,7]) 

print(numbr)


#Removing Elements 

# Remove() : remove by value

rnumbers = [10, 20, 30]
rnumbers.remove(20)
print(rnumbers) #[10,30]

# pop() - Remove by index 

rnumbers.pop(1)  
print(rnumbers) #[10]

numbers.pop()    # removes last element

#updating elements

marks1 = [80, 70, 60]
marks1[1] = 75
print(marks1)

# Searching in List : using in 

nums = [5,10,15]

print(10 in nums)   # True
print(20 in nums)   # False

# searching indaex

print(nums.index(15))  #2
