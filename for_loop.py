#FOR LOOP

#EXERCISE 1

#1.Iterate 0 to 10 using 'for' loop.

#Answer
"""for i in range(0,11,1):
    print(i)
"""


#2.Iterate 10 to 0 using for loop, do the same using while loop.

#Answer
"""for i in range(10,-1,-1):
    print(i)

i=11
while i>0:
    i-=1
    print(i) """


#3.Write a loop that makes seven calls to print(), so we get on the output the following triangle:

""""
*
**
***
****
*****
******
*******
"""

#Answer-Long way
"""user_value = 7
for i in range(1,user_value+1):
    for j in range(i):
        print("*",end="")
    print()"""

#Answer-Short way
"""user_value = 7
for i in range(1,user_value+1):
    print("*"*i)"""


#4.Write a loop that makes 5 calls to print(),so we get on the output the following triangle:

""""
*****
****
***
**
*
"""

#Answer-Long way
"""user_value = 5
for i in range(user_value,0,-1):
    for j in range(i):
        print("*",end="")
    print()"""
#Answer-Short way
"""user_value = 5
for i in range(user_value,0,-1):
    print("*"*i)"""



#5.Write a loop that makes 5 calls to print(),so we get on the output the following triangle:

"""
    *
   **
  ***
 ****
***** 
"""

#Answer-Long way
"""user_value = 5
for i in range(user_value,0,-1):
    for j in range(i-1): #i-1 gives us " " spaces.
        print(" ",end="")
    for k in range(user_value-i+1):
        print("*",end="")
    print()"""
#Answer-Shor way
"""user_value = 5
for i in range(user_value,0,-1):
    print(" " * (i-1) + "*" * (user_value-i+1))"""




#6.Write a loop that makes 5 calls to print(),so we get on the output the following triangle:

"""
*****
 ****
  ***
   **
    *
"""

#Answer-Long way
"""user_value = 5
for i in range(user_value,0,-1):
    for j in range(user_value-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()"""
#Answer-Short way
"""user_value = 5
for i in range(user_value,0,-1):
    print(" " * (user_value-i) + "*" * (i))"""


#7.Write a loop that makes 5 calls to print(),so we get on the output the following triangle:

"""
*********
 *******
  *****
   *** 
    *
"""

#Answer-Long way
"""user_value = 5
for i in range(user_value,0,-1):
    for j in range(user_value-i):
        print(" ",end="")
    for k in range(i*2-1):
        print("*",end="")
    print()"""

#Answer-Short way
"""user_value = 5
for i in range(user_value,0,-1):
    print(" "*(user_value-i) + "*"*(i) + "*"*(i-1)) #In this solution we divide the triangle two pieces the output like this:

***** ****
 **** ***
  *** **
   ** * 
    *
"""

#8.Write a loop that makes 5 calls to print(),so we get on the output the following triangle:

"""  
    *
   ***
  *****
 *******
*********
"""

#Answer-Long way
"""user_value = 5
for i in range(user_value,0,-1):
    for j in range(i-1):
        print(" ",end="")
    for k in range((user_value-i)*2+1):
        print("*",end="")
    print()"""

#Answer-Short way
"""user_value = 5
for i in range(user_value,0,-1):
    print(" "*(i-1) + "*"*(user_value-i+1) + "*"*(user_value-i)) #In this solution we divide the triangle two pieces the output like this:

    *
   ** *
  *** **
 **** ***
***** ****
"""


#9.Write a loop that makes 5 calls to print(),so we get on the output the following equilateral quadrangle:

"""
    *         
   ***  
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

#Answer-Long way
"""user_value = 5
for i in range(user_value,0,-1):
    for j in range(i-1):
        print(" ",end="")
    for k in range((user_value-i)*2+1):
        print("*",end="")
    print()
for m in range(user_value,0,-1):
    for l in range(user_value-m+1):
        print(" ",end="")
    for t in range((m-1)*2-1):
        print("*",end="")
    print()"""

#Answer-Short way
"""user_value = 5
for i in range(user_value,0,-1):
    print(" "*(i-1) + "*"*((user_value-i)*2+1))
for j in range(user_value,0,-1):
    print(" "*(user_value-j+1) + "*"*((j-1)*2-1)) """


#10.Write a loop that makes 5 calls to print(),so we get on the output the following half equilateral quadrangle:

"""
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *
"""

#Answer-Long way
"""user_value = 5
for i in range(user_value,0,-1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(user_value-i+1):
        print("*",end="")
    print()
for m in range(user_value,0,-1):
    for l in range(user_value-m+1):
        print(" ",end="")
    for t in range(m-1):
        print("*",end="")
    print()
"""
#Answer-Short way

"""user_value = 5
for i in range(user_value,0,-1):
    print(" "*(i-1) + "*"*(user_value-i+1))
for j in range(user_value,0,-1):
    print(" "*(user_value-j+1) + "*"*(j-1))"""



#11.Use nested loops to create the following:

"""
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

#Answer-Long way with using nested loops
"""
a=8
for i in range(a):
    for j in range((a-7)*7):
        print("#",end="")
        for k in range(a-7):
            print(" ",end="")
    print()
"""

#Answer-Short way 
"""
a = 8
for i in range(a):
    print(("#"*(a-7) + " "*(a-7))*7)
"""


#12.Print the following pattern:

""""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""

#Answer

"""for i in range(1,11,1):
    pattern = i * i
    print(f"{i} x {i} = {pattern}")"""


#13.Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

#Answer
"""skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in skills:
    print(i)"""

#14.Use for loop to iterate from 0 to 100 and print only even numbers

#Answer
"""for i in range(0,101,2):
    print(i)"""


#15.Use for loop to iterate from 0 to 100 and print only odd numbers

#Answer
"""for i in range(1,100,2):
    print(i)"""




#-----------------------------------------------------------
#EXERCISE 2

#1.Use for loop to iterate from 0 to 100 and print the sum of all numbers.

#Answer
"""total = 0
for i in range(0,101,1):
    total += i
print("The sum of all numbers is",total)"""

#2.Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#Answer
"""total_even = 0 
for i in range(0,101,2):
    total_even += i
print("The sum of all evens is",total_even)
print("-------------------------------")
total_odds = 0
for k in range(1,100,2):
    total_odds += k
print("The sum of all odds is",total_odds)"""

