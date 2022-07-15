# This challenge is to calculate the Body Mass Index of a Person
# Get the user's data
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# Convert the data to integer
int_height = float(height)
int_weight = int(weight)
# Apply the formula using mathematical operator
BMI = (int_weight/(int_height**2))
bmi = int(BMI)
Bmi = str(bmi)
print("Your body mass index is: " + Bmi)

