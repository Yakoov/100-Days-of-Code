# This program calculates the age of a man in weeks, months and years he has left until 90 Years old. Using all out you have learnt so far

print("Answer the question to know the time you have left untill 90 years old")
age = input("What is your current age in Years:\n")
Int_age= int(age)
Years = 90 - Int_age
Days = round((90*365) - (Int_age*365))
Weeks = round((90*52) - (Int_age*52))
Months = round((90*12) - (Int_age*12))

# or
Years = 90 - Int_age
Days = round (Years * 365)
Weeks = round(Years * 52)
Months = round(Years * 12)

print(f"You have {Years} Years, {Days} Days, {Weeks} Weeks, {Months} Months untill 90 Years\nUse it Wisely my Friend ")




# This program calculates the number of days, months and hours used by an individual
print("Answer the questions to know the amount of time you have spent on Earth")
age = input("What is your current age in Years:\n")
Integer_age= int(age)

Day = Integer_age * 365
Weeks = Integer_age *52
Months = Integer_age * 12

print(f"My brother you have walked on this land for {Day} Days, {Weeks} Weeks {Months} Months\nWait think back, How have you spent it ")