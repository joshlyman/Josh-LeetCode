class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numlen = len(nums)
        for i in range(numlen+1):
            if i not in nums:
                return i 

# Time: O(N^2) since in list is O(N)
# Space:O(1)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numlen = len(nums)
        numset = set(nums)
        for i in range(numlen+1):
            if i not in numset:
                return i 
        
# Time: O(N) since in set is O(1)
# Space:O(N)        


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)  
        
# Time: O(N)
# Space:O(1)