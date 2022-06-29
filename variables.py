#EXERCISE 1

# 1.Declare a first name variable and assign a value to it
first_name = "Cem"

print("First name: " , first_name)
print("---------------------------")
#2.Declare a last name variable and assign a value to it
last_name = "Mandracı"

print("Last name: " , last_name)
print("---------------------------")
#3.Declare a full name variable and assign a value to it
full_name = "Cem Mandraci"

print("Full name: " , full_name)
print("---------------------------")
#4.Declare a country variable and assign a value to it
country = "Turkey"

print("Country: " , country)
print("---------------------------")
#5.Declare a city variable and assign a value to it
city = "Kirklareli"

print("City: " , city)
print("---------------------------")
#6.Declare an age variable and assign a value to it
age = 26

print("Age: " , age)
print("---------------------------")
#7.Declare a variable is_married and assign a value to it
is_married = False

print("Married: " , is_married)
print("---------------------------")
#8.Declare multiple variable on one line
full_name , country , city , age , is_married ="Cem Mandraci" , "Turkey" , "Kirklareli" , 26 , False

print(full_name , country , city , age , is_married)
print("---------------------------")

#EXERCISE 2

#1.Check the data type of all your variables

print(type(first_name))
print("*****************")
print(type(last_name)),
print("*****************")
print(type(full_name))
print("*****************")
print(type(country))
print("*****************")
print(type(city))
print("*****************")
print(type(age))
print("*****************")
print(type(is_married))
print("---------------------------")

#2. Find the length of your first name
print("First name length:",len(first_name))
print("---------------------------")

#3.Compare the length of your first name and your last name
print("First name length:",len(first_name))
print("Last name length: ",len(last_name))
print("---------------------------")

#4.Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

#4.1.Add num_one and num_two and assign the value to a variable add_total

add_total = num_one + num_two # Add with '+' sign.
print(add_total)
print("---------------------------")

#4.2.Subtract num_two from num_one and assign the value to a variable subtract_total

subtract_total = num_one - num_two # Subtract with '-' sign.
print(subtract_total)
print("---------------------------")

#4.3.Multiply num_two and num_one and assign the value to a variable multiply_total

multiply_total = num_one * num_two # Multiply with '*' sign.
print(multiply_total)
print("---------------------------")

#4.4.Divide num_one by num_two and assign the value to a variable divide_total

divide_total = num_one / num_two # Divide with '/' sign.
print(divide_total)
print("---------------------------")

#4.5.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

remainder = num_one % num_two #Modulus division with '%' sign.
print(remainder)
print("---------------------------")

#4.6.Calculate num_one to the power of num_two and assign the value to a variable exp

exp = num_one ** num_two # Exponentiation with '**' sign.
print(exp)
print("---------------------------")

#4.7.Find floor division of num_one by num_two and assign the value to a variable floor_division

floor_division = num_one // num_two # Floor division with '//' sign.

print(floor_division)
print("---------------------------")

#5.The radius of a circle is 30 meters

r = 30
pi = 3.14

#5.1.Calculate the area of a circle and assign the value to a variable name of area_of_circle

area_of_circle = pi * r * r # or pi * r**2
print("Area of circle is:",area_of_circle)
print("---------------------------")

#5.2.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

circumference = 2 * pi * r
print("Area of circumference is:",circumference)
print("---------------------------")

#5.3.Take radius as user input and calculate the area.

user_radius = int(input("Please enter radius to calculate area of circle: \n"))
area_circle = pi * user_radius**2
print("Area of circle is:",area_circle)
print("---------------------------")


