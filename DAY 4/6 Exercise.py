# The goal of this exercise is to use what you have learnt so far to place elements inside the boxes
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

# nested list
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure\n")

# Creating a variable for horizontal and vertical position
# e.g a Number position 23 with index position 0 and 1. 2 is the row 3 is the column
# We convert the string input to integer

row = int(position[0])
column = int(position[1])

# remeber list starts counting from "0"
selected_position = map[row -1][column -1] = "X"

print(f"{row1}\n{row2}\n{row3}")