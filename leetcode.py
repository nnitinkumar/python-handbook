##Q : Two sum

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