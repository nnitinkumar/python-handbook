#SOURCE:
https://www.w3schools.com/python/ref_string_split.asp
https://www.geeksforgeeks.org/python-map-function/
https://www.geeksforgeeks.org/sorted-function-python/
https://www.geeksforgeeks.org/python-set-method/
nitin

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
    
#split() method splits a string into a list  

#map() function returns a map object (which is an iterator) of the results after applying
#the given function to each item of a given iterable (list, tuple etc.)

#sorted function sorts any sequence (list, tuple) and always returns a list
#with the elements in a sorted manner, without moddifying the original sequence

#set() method is used to convery any of the iterable to sequence of
#iterable elements with distinct elements
#Sets are unordered. Use sorted(set(sampleList)) to get it sorted 