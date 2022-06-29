#1.Concatenate the string 'My', 'name', 'is', 'Cem' to a single string, 'My name is Cem'.

a = 'My'
b = 'name'
c = 'is'
d = 'Cem'
print(f"{a} {b} {c} {d}")
print("-------------------")

#2.Declare a variable named company and assign it to an initial value "Coding For All".
#Print the variable company using print().
company = "coding For All"
print(company)
print("-------------------")

#3.Print the length of the company string using len() method and print().
print("Length of the company is: ",len(company))
print("-------------------")

#4.Change all the characters to uppercase letters using upper() method.
print(company.upper())
print("-------------------")

#5.Change all the characters to lowercase letters using lower() method.
print(company.lower())
print("-------------------")

#6.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print("-------------------")
print(company.title())
print("-------------------")
print(company.swapcase())
print("-------------------")

#7.Cut(slice) out the first word of Coding For All string.
print(company[0:6])
print("-------------------")

#8.Check if Coding For All string contains a word Coding using the method index, find or other methods
challange = "Coding For All"
sub_string = "All"
print(challange.index(sub_string)) #Result is 11 because 'All' is starting [11:].
print("-------------------")

#9.Replace the word coding in the string 'Coding For All' to Python.
print(challange.replace("Coding","Python"))
print("-------------------")

#10.Split the string 'Coding For All' using space as the separator (split()) .

print(challange.split())
print("-------------------")

#11.What is the character at index 0 in the string Coding For All.
print(challange[0])
print("-------------------")

#12.What is the last index of the string Coding For All.
print(challange[-1])
print("-------------------")

#13.What character is at index 10 in "Coding For All" string
print(challange[10]) #The result is ' ' space.
print("-------------------")

#14.Use rfind to determine the position of the last occurrence of l in Coding For All People.

challange_2 ="Coding For All People"
print(challange_2.rfind("l")) #rfind(): Returns the index of the last occurrence of a substring, if not found returns -1.
print("-------------------") 

#15.Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

challange_3 = 'You cannot end a sentence with because because because is a conjunction'
print(challange_3.find("because")) #find(): Returns the index of the first occurrence of a substring, if not found returns -1.
print("-------------------") 


#16.Does ''Coding For All' start with a substring Coding?
challange_4 = "Coding For All"
print(challange_4.startswith("Coding"))
#-Does 'Coding For All' end with a substring coding?
print(challange_4.endswith("coding"))
print("-------------------") 

#17.The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

python_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = " ".join(python_lib)
print(result)
print("-------------------") 

#18.Use the new line escape sequence to separate the following sentences

"""
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")

"""

print("I am enjoying this challange.\nI just wonder what is next.")
print("-------------------")

#19.Use a tab escape sequence to write the following lines.
"""
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
"""

print("Name\tAge\tCountry\t City\nCem\t250\tTurkey\t Helsinki")
print("-------------------")

#20.Use the string formatting method to display the following:
"""
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
"""

radius_str = 10
area_str = 3.14 * radius_str ** 2
print("The area of a circle with radius {} is {} meters square".format(radius_str,area_str))
print("-------------------")

#21.Make the following using string formatting methods:
"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""

a = 8
b = 6
print(f" {a} + {b} = {a+b} ")
print(f" {a} - {b} = {a-b} ")
print(f" {a} * {b} = {a*b} ")
print(f" {a} / {b} = {a/b:.2f} ")
print(f" {a} % {b} = {a%b} ")
print(f" {a} // {b} = {a//b} ")
print(f" {a} ** {b} = {a**b} ")