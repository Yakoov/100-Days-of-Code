# This Exercise, we going to create a program using for loops that prints out the highest scores or number in a given number
scores = input("Input a list of student scores, seprated by a comma\n").split(",")
for n in range(0, len(scores)):
    scores[n] = int(scores[n])
print(scores) 


score = 0
for highest in scores:
    # print(highest)
    
    if highest >= score:
        score = highest
print(f"The Highest score is: {score}")



