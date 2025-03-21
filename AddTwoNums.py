# Add two numbers in python
# Author: Anbo Xu
# Using a function

# functions to add two numbers
def add(a, b):
    # converting input to float and adding
    res = float(a) + float(b)
    print(res)

# taking user input
a = input("First number: ")
b = input("Second number: ")

# calling function
res = add(a, b)
print("The answer is: ")
print(res)