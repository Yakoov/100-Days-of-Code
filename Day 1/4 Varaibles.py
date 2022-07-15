# A variable is where you store data
# It is like a small box where your put your stuffs and label it
# rules for name a variable
# 1. Never Start with a number 
# 2. Use underscore to seprate words "-" not space " "





# This is the solution to the input coding exercise using variable
Name = input ("What is your name\n")
length = len(Name)
print(length)

# Interactive coding Exercise
# Write a program that switches the balues stored in the variables a and b

a = input("a: ")
b = input("b: ")
# Assigning the input data to another variable makes it easy for switching

c = a
a = b
b = c


print("a = " + a)
print("b = " + b) 
