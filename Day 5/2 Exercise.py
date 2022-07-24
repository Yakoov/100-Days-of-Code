# This exercise, we are going to calculate the average height of students given by the user

# This code converts the string to an integer
student_heights = input("Input a list of student heights, seprated by a comma\n").split(",")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# use for to to add the heights inside the list
# Assign the total height to be zero and iterate using for loop
total_height = 0
for height in student_heights:
    total_height += height
print(f"The Total height of studnet is: {total_height}")

# Repeat the same step above
Number_of_student = 0
for length in student_heights:
    Number_of_student += 1
print(f"The Number of student is: {Number_of_student}")

Average_height = (total_height/Number_of_student)
print(f"The average height of each student is: {Average_height}")

