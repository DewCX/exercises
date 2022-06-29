#EXERCISE 1

#1.Declare an empty list
empyt_list = []

#2.Declare a list with more than 5 items
fruits = ['banana','orange','mango','lemon','apple']

#3.Find the length of your list
print(len(fruits))
print("----------------")

#4.Get the first item, the middle item and the last item of the list
print("First item in the list: ",fruits[0])
print("Middle item in the list: ",fruits[2])
print("Last item in the list: ",fruits[-1])
print("----------------")

#5.Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
#-Print the list using print()

it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies)
print("----------------")

#6.Print the number of companies in the list
print("Number of companies in the list: ",len(it_companies))
print("----------------")

#7.Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[-1]
print(first_company)
print(middle_company)
print(last_company)
print("----------------")

#8.Add an IT company to it_companies
it_companies.append("IT")
print(it_companies)
print("----------------")

#9.Insert an Github company in the middle of the companies list
it_companies.insert(4,"Github")
print(it_companies)
print("----------------")

#10.Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[4].upper())
print("----------------")

#11.Sort the list using sort() method
it_companies.sort()
print(it_companies)
print("----------------")

#12.Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
print("----------------")

#13.Slice out the first 3 companies from the list
slice_first_3_item = it_companies[0:3]
print(slice_first_3_item)
print("----------------")

#14.Slice out the last 3 companies from the list
slice_last_3_item = it_companies[-3::]
print(slice_last_3_item)
print("----------------")

#15.Remove the first IT company from the list
it_companies.remove("IT")
print(it_companies)
print("----------------")

#16.Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)
print("----------------")

"""#17.Destroy the IT companies list
del it_companies
print(it_companies) # This should give: NameError: name 'it_companies' is not defined
print("----------------")"""

#18.Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

#-After joining the lists in question 18. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack = front_end + back_end
print(full_stack)
#insert Python and SQL after redux
front_end.append("Python")
front_end.append("SQL")
print(front_end)
print("----------------")


#-------------------------------------------------
#EXERCISE 2

#1.The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#1.1.Sort the list and find the min and max age

min_ages_list = min(ages)
print(min_ages_list)
max_ages_list = max(ages)
print(max_ages_list)
print("----------------")

#1.2.Add the min age and the max age again to the list
ages.append(min_ages_list)
ages.append(max_ages_list)
print(ages)

#1.3.Find the average age (sum of all items divided by their number )
average = sum(ages) / len(ages)
print("Average of the list is:",average)



