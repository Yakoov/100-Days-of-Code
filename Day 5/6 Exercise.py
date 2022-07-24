# This Exercise, we are going to play the fizzbuzz game
# We will write a program that prints numbers ranging from 1-100
# Rules
# 1. If number is divisible by 3 let it output fizz
# 2. If number is divisible by 5 let it output buzz
# 3. if number is divisble by both 3 and 5 let it output fizzbuzz

number = 0
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)