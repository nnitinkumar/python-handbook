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
        
        