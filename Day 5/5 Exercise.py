# In this exercise, we going to calculate the sum of all the even numbers 1-100

sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum += i
print(f"The total sum of even number in 1-100 is: {sum}")

# also
# we start from 2 because we want a range of even number
total = 0
for i in range(2,101, 2):
    total += i
print(f"The total sum of even number in 1-100 is: {total}")
