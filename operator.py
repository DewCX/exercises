#1.Declare your age as integer variable
age = 26

#2.Declare your height as a float variable
height = 1.78

#3.Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

enter_base = float(input("Please enter base of triangle: \n"))
enter_height = float(input("Please enter height of triangle: \n"))
area_of_triangle = 0.5 * enter_base * enter_height
print("The area of the triangle is: ",area_of_triangle)
print("---------------------")
#4.Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a = float(input("Please enter side a of triangle: \n"))
side_b = float(input("Please enter side b of triangle: \n"))
side_c = float(input("Please enter side c of triangle: \n"))
perimeter_of_triangle = side_a + side_b +side_c
print("The perimeter of the triangle is: ",perimeter_of_triangle)
print("---------------------")

#5.Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = float(input("Please enter length of rectangle: \n"))
width = float(input("Please enter width of rectangle: \n"))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print("The area of the rectangle is: ",area_of_rectangle)
print("---------------------")
print("The perimeter of the rectangle is: ",perimeter_of_rectangle)
print("---------------------")

#6.'I hope this course is not full of jargon.' Use 'in' operator to check if jargon is in the sentence.

sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)
print("---------------------")
#7.Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hour = float(input("Please enter hour:"))
rate_per_hour = float(input("Please enter per hour: "))
earning = hour * rate_per_hour
print("Your weekly earning is:",earning)
print("---------------------")
#8.Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

user = int(input("Please enter number fo years: \n"))
number_of_seconds = 60*60*24*365*user
"""
1 year = 365 days
1 day = 24 hours
1 hour = 60 minutes
1 minutes = 60 seconds
"""
print(f"You have lived for {number_of_seconds} seconds")
