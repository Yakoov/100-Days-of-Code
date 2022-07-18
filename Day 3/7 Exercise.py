# This coding exercise uses all what we have been taught so far to build a love calculator
print("Welcome to the Love Calclator\nGet ready to find your True Love")
name_1 = input("What is your name? \n")
name_2 = input("What is their name? \n")

# Combine both names
name = name_1 + name_2
# Convert the user input to lower case with the ".lower()"
lower_name = name.lower()
# Counting the letter "true" in the lower_name

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t + r + u + e

# Counting the letter "love" in the lower_name

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

love = l + o + v + e

# Combine the two integers together as a string to get the score
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}. you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}. you are alright together")
else:
    print(f"Your score is {love_score}.")
