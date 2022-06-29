#EXERCISES 1

#1.Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

"""
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""
#Answer
"""user_age = int(input("Enter your age: "))
under_18_user = 18-user_age

if user_age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {under_18_user} more years to learn to drive.")"""

#2.Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

"""
Enter your age: 30
You are 5 years older than me.
"""

#Answer
"""user_age = int(input("Enter your age: "))
my_age = 26

if my_age > user_age:
    print(f"I am {my_age-user_age} years older than you.")
else:
    print(f"You are {user_age-my_age} years older than me.")"""

#3.Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

"""
Enter number one: 4
Enter number two: 3
4 is greater than 3
"""

#Answer

"""number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))

if number_one > number_two:
    print(f"{number_one}(number one) is greater than {number_two}.")
else:
    print(f"{number_two}(number two) is greater than {number_one}.")"""


#-------------------------------------------------
#EXERCISE 2


#1.Write a code which gives grade to students according to theirs scores:

"""
90-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""

#Answer

"""student_grade = float(input("Please enter your grade: "))

if student_grade>=90 and student_grade<=100:
    print("Your grade code is A.")
elif student_grade>=70 and student_grade<=89:
    print("Your grade code is B.")
elif student_grade>=60 and student_grade<=69:
    print("Your grade code is C.")
elif student_grade>=50 and student_grade<=59:
    print("Your grade code is D.")
elif student_grade>=0 and student_grade<=49:
    print("Your grade code is F.")
else:
    print("Your grade value must be between 0-100 !!")"""


#2.Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

#Answer

"""user_value = str(input("Enter month: "))

if user_value == "September" or user_value == "October" or user_value == "November":
    print("The season is Autumn.")
elif user_value == "December" or user_value == "January" or user_value == "February":
    print("The season is Winter.")
elif user_value == "March" or user_value == "April" or user_value == "May":
    print("The season is Spring.")
elif user_value == "June" or user_value == "July" or user_value == "August":
    print("The season is Summer.")
else:
    print("Please enter name of months.")"""

#3.The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

#-If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')


#Answer
"""user_value_fruit = str(input("Please enter name of fruit: "))

if user_value_fruit in fruits:
    print("That fruit already exist in the list.")
elif user_value_fruit not in fruits:
    fruits.append(user_value_fruit)
    print("Modified list",fruits)"""


#4.Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Cem',
    'last_name': 'Mandracı',
    'age': 26,
    'country': 'Turkey',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }


#4.1.Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
"""if 'skills' in person:
    print("Middle skill in the skills list is: ",person['skills'][2])    """

#4.2.Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
"""if 'skills' in person:
    if 'Python' in person['skills']:
        print("Yes")
    else:
        print("No")"""


#4.3. If the person is married and if he lives in Finland, print the information in the following format:
 
"""if person['is_married']==False and person['country']=='Turkey':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}.He is not married.")"""
    

