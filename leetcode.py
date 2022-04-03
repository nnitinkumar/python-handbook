https://leetcode.com/tag/string/    

##1Q : Two sum

#nums is the given list 
#nums = [2,7,11,15]

#target is the added up result which we require
#target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]
                    
                    
 -----------------------------------------------------------------
 
 ##Q : Convert a list into a string
 
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays)
print(listAsString)

 -----------------------------------------------------------------

##1119 : Remove vowels from a string

class Solution:
    def removeVowels(self, S: str) -> str:
    
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        new_word = ""
        
        for letter in S:
            if(letter not in vowels):
                new_word += letter
             
        return new_word
        
        
 -----------------------------------------------------------------        
 
##2114 : Maximum number of words found in sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for i in sentences:
            m = max(m, i.count(" ") + 1)
        return m 
        

-----------------------------------------------------------------    

##58 : Length of last word

-----------------------------------------------------------------
#https://docs.python.org/release/2.3.5/whatsnew/section-slices.html

##9: Palindrome number

#Exp and example
#given an integer x, return true if x is palindrome integer
#121 is a palindrome
#123 is not 

def isPalindrome(input_string):
    return s == s[::-1]
    

#Driver code
input_string = "nitin"

checked = isPalindrome(input_string)

if checked:
    print("Yes")
else:
    print("No")
    
-----------------------------------------------------------------

#13: Ronam to numeral

IV is 5
IX is 9
XL is 40
XC is 90
CD is 400
CM is 900

E.G.
LVIII
L + V + I + I + I
50 + 5 + 1 + 1 + 1

MCMXCIV
M + C + M + X + C + I + V

1000 + 100 + 1000 + 10 + 100 + 1 + 5
2306


M + CM + XC + IV
1000 + 900 + 90 + 4
1994

--Psuedo code
case when 
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

if I is before V then V - 1 i.e. 5-1 = 4
if I is before X then X - 1 i.e. 10-1 = 9
 
if X is before L then L - 10 i.e. 50-10 = 40
if X is before C then C - 10 i.e. 100-10 = 90

if C is before D then D - 1 i.e. 500-100 = 400
if X is before M then M - 1 i.e. 1000-100 = 900







