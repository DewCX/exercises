#EXERCISE

#1.Create an empty dictionary called dog
dog = {}

#2.Add name, color, breed, legs, age to the dog dictionary

dog = {
    "name":"Ghost",
    "color":"White",
    "Breed":"Dog-wolf",
    "Legs":4,
    "Age":5
}
print(dog)
print("------------------------")

#3.Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    "first_name":"Cem",
    "last_name":"Mandracı",
    "gender":"Male",
    "age":26,
    "marital_status":"Single",
    "skills":["Python","HTML","CSS","JavaScript","Boostrap"],
    "adress":{
        'street':"Space street",
        'zipcode':"39750"
    }
}

#4.Get the length of the student dictionary

print("The number of dictionary student is: ",len(student))
print("------------------------")

#5.Get the value of skills and check the data type, it should be a list

print(student["skills"])
print(type(student["skills"]))
print("------------------------")

#6.Modify the skills values by adding one or two skills

student["skills"].append('React')
print(student["skills"])
print("------------------------")

#7.Get the dictionary keys as a list
keys = student.keys()
print(keys)
print("------------------------")

#8.Get the dictionary values as a list
values = student.values()
print(values)
print("------------------------")

#9.Change the dictionary to a list of tuples using items() method

print(student.items())
print("------------------------")

#10.Delete one of the items in the dictionary
del student["marital_status"]
print(student)
print("------------------------")

#11.Delete one of the dictionaries
del dog