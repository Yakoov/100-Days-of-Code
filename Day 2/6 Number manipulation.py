# In python me whave different mathematical operation
# We use the round() function to round number
# e.g round(8/3, 2) it rounds the number to 2 d.p places

print(round(8 / 2, 2))
print(round(2.66666666, 2))

# Floor division (//), This division removes all decimals, and make it an integers
# it converts a float number to an integer
print(8 // 3)

# This += or -= or /= or *= allows you to avoid repition
# This code below are the same 

score= 0
# User scores a point
score = score + 1
print(score)
# This code can also be written as
grade = 0
grade += 1 
print(grade)

# F strings
# f strings make it easy to mix strings and different datatypes
# f"string {datatype}"

Mark = 0
height = 1.8
isWinning = True
 
print (f"your mark is {Mark}, your height is {height}, your are winning is {isWinning}")
