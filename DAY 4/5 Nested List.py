# Nested List is a list inside of another List 

Main_list = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes', 'Celery', 'Potatoes']

fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
veggies = ['Tomatoes','Spinach', 'Kale', 'Celery', 'Potatoes']

nested_list = [fruits,veggies]
print(nested_list)

# This will print the nested_list first counting the fruits then second bracket will count the item inside the fruits
print(nested_list[0][1])
