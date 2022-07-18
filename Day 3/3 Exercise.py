# Using the elif statement
# The "elif" statement allows for mutiple if else block

# Write a program that interprets the Body Mass Index basedon a user's weight and heigh
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round((weight) / (height)**2, 2)

if BMI < 18.5:
    print(f"Your Need to add up, your are under weight\nYour weigh {BMI}")
elif BMI < 25:
    print(f"You are normal man, Your need some exercise\nYour BMI is {BMI}")
elif BMI < 30:
    print(f"You are overweight, you need to diet nigga.\nYour BMI is {BMI}")
elif BMI < 35:
    print(f"You are  obese, Help yourself.\nYour BMI is {BMI}")
else:
    print(f"You are clincally obese.\n Your BMI is {BMI}")