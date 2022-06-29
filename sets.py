#EXERCISE 1

#sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
ages = [22, 19, 24, 25, 26, 24, 25, 24]


#1.Find the length of the set it_companies
print("The length of the it_companies are: ",len(it_companies))
print("-----------------------")

#2.Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
print("-----------------------")

#3.Insert multiple IT companies at once to the set it_companies

it_companies.update(["Github","Ebay","LinkedIn"])
print(it_companies)
print("-----------------------")

#4.Remove one of the companies from the set it_companies

it_companies.remove("Oracle")
print(it_companies)
print("-----------------------")

#-------------------------------------------------
#EXERCISE 2

#1.Join A and B
C = A.union(B)
print(C)
print("-----------------------")

#2.Find A intersection B
a_to_b_intersection = A.intersection(B)
print(a_to_b_intersection)
print("-----------------------")

#3.Is A subset of B
is_subset = A.issubset(B)
print(is_subset)
print("-----------------------")

#4.Are A and B disjoint set
is_disjoint = A.isdisjoint(B)
print(is_disjoint)
print("-----------------------")

#5.What is the symmetric difference between A and B

## it means (A\B)∪(B\A)
symmetric_difference_a_b = A.symmetric_difference(B)
print(symmetric_difference_a_b)
print("-----------------------")

#6.Delete the sets completely
del A
del B


#--------------------------------------------------
#EXERCISE 3

#1.Convert the ages to a set and compare the length of the list and the set, which one is bigger?

print("List of ages length are : ",len(ages))
ages = set(ages)
print("Sets of ages length are : ",len(ages))
#Number of list > number of sets



