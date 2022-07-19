# This exercise, we are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
# Instruction: Don't use the "choice()" function
# We would be using all what we have been taught so far

# We would also be using the "split()" function to convert a string to list
# The split(",") will sperate the string to a list by a comma, it works based on the character specified in it

names_string = input("Give me every body's name seprated by a comma and a space\n")
names = names_string.split(", ")

# We have to import random since we dealing with random selection
import random

# We get the length of of the list so we can randomly select using numbers
Length_names = len(names)

# we use the random function to generate random numbers between 0 and the length of the list
# "-1" included because counting in python starts from "0"s
final_names = random.randint(0,Length_names-1)

# using string concatation 
print(names[final_names] + " is going to pay the bills today")

# or we could also use the randrang
# import random
# Final_names = random.randrange(0,len(names)-1)
# print(names[Final_names])

# import random
# Final_names = random.randint(0,len(names)-1)
# print(names[Final_names])

# Using the random "choice()" function
# This function just randomly select the items from the list, so code from line 16 aren't needed
print(random.choice(names))