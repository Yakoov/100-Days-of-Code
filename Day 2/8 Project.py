# This Project requires the application of what has been learnt so far
# This is a tip calculator.

print("Welcome to the tip calculator\nLet's help you split the bill")
Bill = float(input("What is the total bill?\n$"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12 or 15\n"))/100
people = int(input("How many people do you want to split the bill among?\n"))

calc_bill = (Bill * percent_tip) + Bill
bill_person = round(calc_bill/people, 2)
# This code below allows us to round to 2 d.p with a zero
Total = "{:.2f}".format(bill_person)
print(f"Each people should pay: ${Total} ")
