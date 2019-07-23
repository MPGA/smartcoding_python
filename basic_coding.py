"""
Python does offer magic methods like sum() and others, please try to write down your algorithms or coding 
instructions clearly without using any shortcuts
"""

# Multiply 3 and any number
def mult(number):
    return number*3

    
# adds two numbers together
def add(a, b):
    return a+b


"""
Using data structures like list, can you find the total or the values in that list.
Do not use a function like sum(someList), that would be cheating ;-)
"""
# Data structure
numbers = [1,2,3,6]
def sumOfListNumbers(someList):
    return numbers[0] + numbers [1] + numbers[2] + numbers[3]

    

# Program checker (do not change the lines below)    
assert sumOfListNumbers(numbers) == 12
assert mult(3) == 9
assert add(1,3) == 4
print("assert num.1: " + str(sumOfListNumbers(numbers)))
print("assert num.2: " + str(mult(3)))
print("asset num.3: " + str(add(1,3)))
print("total sum of all asserts: " + str(sumOfListNumbers(numbers) + mult(3) + add(1,3)))