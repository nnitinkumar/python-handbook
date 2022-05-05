  

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