# Write a program that adds the digits in a 2 digit number e.g if the input was 35, then the output should be 3+5

two_digit_number = input("Type a two digit number: ")
# Subscripting the string or using string slicing
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# convert the string to an integer, when we use input function, It always store a string regardless of the input
result_1=int(first_digit)
result_2=int(second_digit)
# Add the two integers together
Result = result_1 + result_2
print(Result)
