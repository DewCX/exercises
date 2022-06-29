#EXERCISE 1

#1.Create an empty tuple
empty_tuple=()

#2.Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers=("Ahmet","Mehmet")
sisters=("Ayşe","Fatma")

#3.Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
print("-----------------")

#4.How many siblings do you have?
print("The number of siblings are: ",len(siblings))
print("-----------------")

#5.Modify the siblings tuple and add the name of your father and mother and assign it to family_members

father_mother_names = ("Yaşar","Filiz")
family_members = siblings + father_mother_names
print(family_members)
print("-----------------")

#----------------------------------------------
#EXERCISE 2

#1.Unpack siblings and parents from family_members

"""del family_members
print(family_members) #NameError: name 'family_members' is not defined
print("-----------------")"""

#2.Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Apple","Banana","Melon","Mango")
vegetables = ("Cucumber","Carrot","Tomato","Potato")
animals = ("Cat","Dog","Bird","Turtle")
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)
print("-----------------")

#3.Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print("-----------------")

#4.Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

middle_items = food_stuff_lt[0:6]
print(middle_items)
print("-----------------")

#5.Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[0:3]
print("First three items are: ",first_three_items)
last_three_items = food_stuff_lt[-3::]
print("Last three items are: ",last_three_items)
print("-----------------")

#6.Delete the food_staff_tp tuple completely
del food_stuff_tp

#7.Check if an item exists in tuple:

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

#7.1.Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

#7.2.Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)