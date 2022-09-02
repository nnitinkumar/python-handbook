  

#Q:Find the runner up score

'''
Given the participants's score sheet for your 
university, find the runner up. You are given n scores.
Store them in a list and find the score of the runner up
'''

#Using Sets
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print (sorted(set(arr))[-2])
    
#EXPLANATION:     
#split() method splits a string into a list  

#map() function returns a map object (which is an iterator) of the results after applying
#the given function to each item of a given iterable (list, tuple etc.)

#sorted function sorts any sequence (list, tuple) and always returns a list
#with the elements in a sorted manner, without moddifying the original sequence

#set() method is used to convery any of the iterable to sequence of
#iterable elements with distinct elements
#Sets are unordered. Use sorted(set(sampleList)) to get it sorted 

#SOURCE:
https://www.w3schools.com/python/ref_string_split.asp
https://www.geeksforgeeks.org/python-map-function/
https://www.geeksforgeeks.org/sorted-function-python/
https://www.geeksforgeeks.org/python-set-method/


------------------------------------------------------------------------------
#Q: Nested Lists

'''
Given the names and grades for each student in a class of N
students, store them in a nested list and print the name(s)
of any student(s) having the second lowest grade
'''

#####Q Find the difference between 2 and 3 versions


#####Python 2.7
d = {} #Step1-  empty dictionary

for _ in range(int(raw_input())): #Step2 - Range for number of students
    Name = raw_input() #Step3 -  Accepting name of the student
    Grade = float(raw_input())) #Step4 - Accepting the grade of the student
    d[Name] = Grade #Step5 - Assigning name as key and grade as value for the dic
  
v = d.values() #Step6 - Obtaining the values of dic (all grade of students)

second = sorted(list(set(v)))[1] #Step7 - Removing duplicate grade by using set data type, changing to list, sorting in ascending order and taking the second lowest grade

for key, value in d.items(): #Step9 - Going through the name and grade of each student by using items() method of dictionary

        if value == second: #Step10 - Checking whether the grade is equal to the second lowest grade
        
            second_lowest.append(key) #Step11 -- if yes, append it to the second_lowest list
            
second_lowest.sort() #Step 12 - Sorting the name of students  in ascending order

for name in second_lowest: #Step13 - Going through the name each students who got the second lowest grade

   print name #Step 14 - Printing each name of studnets in separate line


#####Python 3

#Number of students
n = int(input())

#Students and grade lists
nameList = []
gradeList = []

#Importing values
if __name__ == '__main__':
    for _ in range(n):
        name = input()
        score = float(input())
        nameList.append((score,name))
        gradeList.append(score)
        
#Define final lists
finalNameList = nameList[:]
finalGradeList = []
finalList = []

#Removing unwanted values
for i in range(n):
    if nameList[i][0] == min(gradeList):
        finalNameList.remove(nameList[i])
        
#Final grade list creation
for i in range(len(finalNameList)):
    finalGradeList.append(finalNameList[i][0])
    
#Adding wanted values
for i in range(len(finalNameList)):
    if finalNameList[i][0] == min(finalGradeList):
        finalList.append(finalNameList[i][1])

#Sorting the list
finalList.sort()

#Print result
for i in range(len(finalList)):
    print(finalList[i])


        
 ------------------------------------------------------------------------------
 '''
 #Q :  Consider a list. You can perform the following commands:
 
 1. insert i e : insert integer e at position i
 2. print : print the list
 3. remove e  : delete the first occurence of integer e
 4. append e : insert integer e at the end of the list
 5. sort : sort the list
 6. pop : pop the last element from the list
 7. reverse : reverse the list
 
 initialize your list and read in the value of n followed by n
 lines of commands where each command will be of the 7 types listed above,
 iterate through each command in order and perform the corresponding
 operation on your list
 '''
 
 '''
intial thoughts:
does not look like a very tough problem
but how to start

 '''
 
 
 ------------------------------------------------------------------------------
#Swap Case
'''
You are given a string and you have to convert all lowercase to uppercase
and vice versa
'''


#Without using inbuilt swapcase function

def swap_case(s):  #Passing string as s
    result = ""
    for letter in s:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
 ------------------------------------------------------------------------------
 
 #Finding the percentage
 
 '''
 Given is a dictionary contaiing key value pairs of name and marks for a list of students
 Print the average of marks array for the student name provided
 Show 2 places after the decimal
 '''
 
if __name__ == '__main__':
  n == int(input())
  student_marks = {}
  for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
   query_name = input()
   marks = student_marks[query_name]
   print(format(sum(marks)/3, '.2f'))
   
 ------------------------------------------------------------------------------   

'''
String split and join  
You are given a string. Split the string on a "" delimeter and join using a - hyphen

''' 

 ------------------------------------------------------------------------------


##What's your name
'''
You are given the firstname and lastname of a person on two
different lines. Your task is to read them and print the 
following:

Hello fistname lastname! You just delved into python.
'''


# Complete the 'print_full_name' function below.

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last

def print_full_name(first, last):
    # Write your code here
    print("Hello {} {}! You just delved into python.".format(first_name, last_name))
    return 

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)  
    
    
 ------------------------------------------------------------------------------
 
##Lists

'''
Consider a list 
list = []

Perform the following commands:
insert i e
print
remove e
append e
sort
pop
reverse

Initialize your list and read in the value of n
followed by n lines of commands
where each command will be of the 7 types
Iterate through each command in order and perform the operation

''' 
'''
Example

N = 4
append 1
apped 2
insert 3 1
print
'''


if __name__ == '__main__':
    N = int(input())
    lis = list()
    for _ in range(N):
        s = input().strip().split(" ")
        if s[0] == "insert":
            lis.insert(int(s[1]),int(s[2]))
        if s[0] == "print":
            print(lis)
        if s[0] == "remove":
            lis.remove(int(s[1]))
        if s[0] == "append":
            lis.append(int(s[1]))
        if s[0] == "sort":
            lis.sort()
        if s[0] == "pop":
            lis.pop()
        if s[0] == "reverse":
            lis.reverse()
           
           
 ------------------------------------------------------------------------------

##Tuples

'''
Given an integer n, n space separated integers as input
Create a tuple t, of those n integers
Then compute and print the result of hash(t)
'''


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = tuple(integer_list)
    print(hash(t))
    
 ------------------------------------------------------------------------------
    
##Exceptions

'''
You are given 2 values a and b
Perform integer division and print a/b

First line contains T, the number of test cases
Next T lines eac contain the space separated values of a and b

Print the value of a/b
In the case of ZeroDivisionError or ValueError, print the error code
'''

for i in range(int(input())):
    try:
        a,b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:", e)
        
 ------------------------------------------------------------------------------
        
##Find a string

'''
The user enters a string and a substring. Print the number of times that the substring occurs in the 
given string.
String traversal will take place from left to right only

First line of input contains the original string. The next line contains the substring

Output the integer number indicating the total number of occurrences of the substring
'''

def count_substring(string, sub_string):
    count = 0 
    i = string.find(sub_string)
    while i != -1:
        count += 1
        i = string.find(sub_string. i+1)
    return count     
       
if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count 
    
 ------------------------------------------------------------------------------


## String split and join

'''
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen

'''


'''
Example:

a = "this is a string"
a = a.split(" ") ##a is now converted into a list of strings
print a 

['this', 'is', 'a', 'string']
'''

def split_and_join(line):
    return "-".join(line.split())
    
if __name__ = '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
    
 ------------------------------------------------------------------------------
 
 ## Mutations
 
 '''
 Lists = mutable
 Tuple = immutable 
 
 Read a given string, change the character at a given
 index and then print the modified string
 '''
 
 def mutate_string(string, position, character):
    s = list(string)
    s[position] = character
    string = "".join(s)
    return string 
 
 if __name__== '__main__':
    s = input()
    i,c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
 ------------------------------------------------------------------------------
 
 ## String Validators
 
 '''
  Python has inbuilt string validation methods for basic data. It can check if a string
 is composed of alphabetical characters, alphanumeric characters, digits etc.
 
 Task:
 You are given a string S.
 Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits,
 lowercase and uppercase characters
 
 '''

if __name__ == "__main__":
    s = input()
    for check in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any({getattr(char, check)() for char in s}))
    
 
 ------------------------------------------------------------------------------

 ## Text alignment
 
 '''
 You are given a partial code that is used to generate the hacker rank
 logo of variable thickness. Your task is to replace the blank (_____)
 with rjust, ljust, center
 '''
 
 
 
 
 
 
 
 
 ## Text wrap 
 
 
 
 
 ##The Minion Game
 
 '''
 Kevin and Stuart want to play the minion game
 
 Game rules:
 Both players are given the same string S.
 Both players have to make substrings using the letters of the string S.
 Stuart has to make words starting with consonants.
 
 
 
 
 
 
 Kevin has to make words starting with vowels.
 The game ends when both players have made all possible substrings.
 
 '''
 
 
 
 ## Capitalize
 
 '''
 You are given a full name, your task is to capitalize the first letter 
 of the first name and second name
 
 '''
 
 
 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.

def solve(s): 
    l = [word.capitalize() for word in s.split(' ')] 
    s = ' '.join(l)  
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


##String formatting 

'''
Given an integer n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

print_formatted function has following parameters:
int number - the maximum value to print

The four values must be printed on a single line in the order
specified above for each i from 1 to number. Each value should be
spaced padded to match the width of the binary value of number 
and the values should be separated by a single space.

Sample input:
17

Sample output:
1 1 1 1
2 2 2 10
..
..
..
17 21 11 1001

'''

'''
Psuedo Code:

We just need to do the conversion.
And apply loop.

'''

def print_formatted(number):
    #your code
    w = len(bin(number)[2:1])
    for i in range(1, number+1):
        print(str(i).rjust(w,""), end = " ")
        print(str(oct(i))[2:].rjust(w," "), end = " ")
        print(str(hex(i))[2:].upper().rjust(w," "), end = " ")
        print(str(bin(i))[2:].rjust(w, " "))


if __name__ == '__main__':
    n = int(inpu())
    print_formatted(n)    
    
    
##Arrays

'''
The Numpy package helps us manipulate large arrays and matrices
of numeric data.

A Numpy array is a grid of values. They are similar to lists,
except that every element of an array must be the same type.


You are given a space separated list of numbers.
Your task is to print a reversed Numpy array with the element
type float.

'''

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    return numpy.array(arr, float)
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)





##Transpose and Flatten





'''
We can generate the transposition of an array using the tool numpy.transpose
It will not affect the original array, but it will create a new array

The tool flatten creates a copy of the input array flattened to one dimension.

'''

import numpy

my_array = numpy.array([1,2,3]), [4,5,6])
print numpy.transpose(my_array)


import numpy

my_array = numpy.array([1,2,3],[4,5,6])
print my_array.flatten()

import numpy

n,_ = input().split()
l = []
for i in range(int(n)):
    m = list(map(int,input().split()))
    l.append(m)
print(numpy.transpose(numpy.array(l,int)))
print((numpy.array(l,int)).flatten())


##Text alignment

'''
In python, a string of text can be aligned left, right or center

.ljust(width) -  returns a left aligned string of length width
.center(width) - returns a centered string of length width
.rust(width) - returns a right aligned string of length width

You are given a partial code that is used for generating the hackerrank logo
of variable thickness. Your task is to replace the blank(____) with rjust,
ljust, center.


'''

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
    
    
    
##Text wrap

'''
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width W.

E.g. ABCDEFGHIJK
4

ABCD
EFGH
IJK


'''

## using recursion

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
## Designer door mat

'''
Mr Vincent works in a door manufacturing company. He designed a new door mat
size - n x m
n is odd number
m is 3 times N

The design should have 'WElcome' written in the center

The design pattern should only use |, . and - characters
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT


R, C = map(int,input().split(' '))

for i in range(1,R,2):
    print((".|."*i).center(C, '-'))  #To print the above triangle

print("WELCOME".center(C,'-')) #To print the welcome

for i in range(R-2,-1,-2):
    print((".|."*i).center(C, '-'))  #To print the lower triangle



## Alphabet Rangoli

'''
You are given an integer N. Your task is to print an alphabet rangoli of size N.

Function description
Rangoli function has following parameters:
Int size - the size of the rangoli

Returns
String - a single string made up of each of the lines of the rangoli separated by a newline character(\n)

Input format 
Only one line of input containing size, the size of the rangoli

Constraints
0<size<27

'''
##Not working
def print_rangoli(size):
    #your code
    characters = string.ascii_lowercase
    lst = []
    width = 4*size - 3
    for i in range(size):
        s = '-'.join(characters[i:size])
        lst.append((s[::-1] + s[1:]).center(width, '-'))
    print('\n'.join(lst{:0:-1] + lst))
    
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
    
#Alternate solution
                        
    
## Capitalize

'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.

chris alan -> Chris Alan

'''

#!/bin/python3

import math
import os
import random
import re
import sys

#Complete the solve function below.
def solve(s):


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()
    
    result = solve(s)
    
    fptr.write(result + '\n')
    
    fptr.close()
    
    
## itertools.product()

'''
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product (A,B) returns the same as ((x,y) for x in A for y in B)

'''
    
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))    
  
  
## collections.counter()

'''
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.


from collections import Counter

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print Counter(myList)
Counter({2: 4, 3:4, 1:3, 4:2, 5:1})

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customer who are willing to pay xi amount of money only if they
get the shoe of their desired size.
Your task is to compute how much money Raghu earned.

'''

n = int(input())

stock = list(map(int,input().split(' ')))

from collections import Counter

Dict = Counter(stock)

x = int(input())

p=0

for i in range(x):
    size, price = map(int, input().split(' '))
    
    if dict(size):
        dict(size)-=1
        p = p*price
 
print(p)

  
##itertools.permutations()

'''
This tools returns successive r length permutations of elements in an iterable.
If r is not specified or is None, then r defaults to the length of the iterable, all
possible full length permutations are generated.

Permutations are printed in a lexicogaphic sorted order.
So, if the input iterable is sorte, the permutations tuples will be produced in a sorted order.

'''


from itertools import permutations
s,n = input().split()



##Alphabet Rangoli







    