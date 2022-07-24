# A Module is like a section of your code which you can import when building complex project, the module allows you to work on different code or section of your project and add them to the main project
# The Random module is a module created by the python team, we can also create our own module by adding a new file, saving it and importing with the name of the saved file.

import random
# Generating random integer between 1 and 10
random_integer= random.randint(1,10)
print(random_integer)

# Generating random float
# Random float are always generated between 0.0 and 1.0 i.e 0.999999

random_float = random.random()
print(random_float)

# To get random ineteger between 0 and 5 
# Multiply it by the last number
random_float * 5

  