# We will be learning how to use Logical operator to combine different operation
#  "and" Opertor: Both conditions "A" and "B" have to be true for the entire Statement to be TRUE. If one is True and the other False, then the entire Statement is "FALSE"
# "or" Operetor: only one condition has to be true for the statement to be "True". Both condition has to be false for the statement to be "False"
# "not" Operator reverses a condition, if the condition or statement is "True" then it become "False" and vice vers

# roller coaster ride
print("Welcome to the rollercoasster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")

    # Logical operator
    
    elif age >=45 and age <= 55:
        print("It's gonna be okay have a free ride")
    
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo takken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")