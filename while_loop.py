#WHILE LOOP

#EXERCISE

#1.Iterate 0 to 10 using 'while' loop.

#Answer
"""i=0
while i<10:
    i+=1
    print(i)"""


#2.Write a while loop that makes seven calls to print(), so we get on the output the following triangle:

""""
*
**
***
****
*****
******
*******
"""

#Answer

"""i = 1
while i <=7:
    j = 1
    while j <= i:
        print("*",end="")
        j += 1
    print()
    i += 1"""


#3.Write a while loop that makes 5 calls to print(),so we get on the output the following triangle:

""""
*****
****
***
**
*
"""

#Answer
"""i = 5
while i>=1:
    j = i
    while j >= 1:
        print("*",end="")
        j -= 1
    print()
    i -= 1"""



#4.Write a loop that makes 5 calls to print(),so we get on the output the following triangle:

"""
    *
   **
  ***
 ****
***** 
"""

#Answer
"""rows = 5
i = rows
while i>=1:
    k=1
    while k<i:
        print(" ",end="")
        k+=1
    j = rows
    while j >= i:
        print("*",end="")
        j-=1
    print()
    i-=1"""

#5.Write a while loop that makes 5 calls to print(),so we get on the output the following triangle:

"""
*****
 ****
  ***
   **
    *
"""

#Answer
"""rows = 5
i = rows
while i>=1:
    j = rows
    while j > i:
        print(" ",end="")
        j-=1
    k=1
    while k<=i:
        print("*",end="")
        k+=1
    print()
    i-=1"""


#6.Write while  loop that makes 5 calls to print(),so we get on the output the following triangle:

"""
*********
 *******
  *****
   *** 
    *
"""

#Answer
"""rows=5
i = rows
while i>=1:
    j = rows
    while j > i:
        print(" ",end="")
        j -= 1
    k = (i*2)-1
    while k>=1:
        print("*",end="")
        k -= 1
    print()
    i -= 1"""

#7.Write while loop that makes 5 calls to print(),so we get on the output the following triangle:

"""  
    *
   ***
  *****
 *******
*********
"""

#Answer
"""rows=5
i = rows
while i > 0:
    j = i
    while j>1:
        print(" ",end="")
        j -= 1
    k = (rows*2)+1
    while k>i*2:
        print("*",end="")
        k -= 1
    print()
    i -= 1"""

#8.Write while loop that makes 5 calls to print(),so we get on the output the following equilateral quadrangle:

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

#Answer
"""kullanici = 5
i=kullanici
while i>0:
    print(" "*(i-1)+"*"*(kullanici+1-i)+"*"*(kullanici-i))
    i-=1
i = kullanici -1
while i>0:
    print(" "*(kullanici-i)+"*"*i+"*"*(i-1))
    i-=1"""


#9.Write while loop that makes 5 calls to print(),so we get on the output the following half equilateral quadrangle:

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

#Answer
"""kullanici = 5
i=kullanici
while i>0:
    print(" "*(i-1)+"*"*(kullanici+1-i))
    i-=1
i = kullanici -1
while i>0:
    print(" "*(kullanici-i)+"*"*i)
    i-=1"""