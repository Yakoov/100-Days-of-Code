#  A list is a way of Organizing and storing data in python
#  A list is made or stored in square brackets "[]"

# This is a list containing all the states of america
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", 
"North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", 
"Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", 
"Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# we can call the list or a state in the list by using square brackets with the number placement of the item e.g states_of_america[0]
# Counting in python always start from 0
# We can also start counting from backwards using the negative index starting from [-1]

print(states_of_america[2])
print(states_of_america[-2])

# We could also change items in a list
states_of_america[1]="Nigeria"
print(states_of_america)

# We could also add items to the end of a list using the funciton called "append()". This add a single item to end of the list
states_of_america.append("JerryLand")
print(states_of_america)

# We could add lots of item to the list by using the extend function
states_of_america.extend(['ReginaLand', 'AgnesLand','Jacoblands'])
print(states_of_america)