#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
# assume character = 4
# We added plus one to pick the last value
for character in range(1,nr_letters + 1):
    password += random.choice(letters)

for character in range(1, nr_symbols +1):
    password += random.choice(symbols)

for character in range(1,nr_numbers + 1):
    password += random.choice(numbers)

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# add to a list and not a string
# use the append function to add items to a list
password_list = []
for character in range(1,nr_letters + 1):
    password_list.append(random.choice(letters))

for character in range(1, nr_symbols +1):
    password_list.append (random.choice(symbols))

for character in range(1,nr_numbers + 1):
    password_list.append(random.choice(numbers))

# using the "shuffle()" function to reorder the list
random.shuffle(password_list)

# let's convert the list to a string using for loops

password = ""
for character in password_list:
    password += character

print(f"Your password is {password}")

print(password_list)