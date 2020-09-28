class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        
        for indx in range(0,len(nums)):
            i = nums[indx]
            if target - i in lookup:
                return [lookup[target-i],indx]
            lookup[i] = indx 

 # Time Complexity: O(n)
 # Space Complexity: O(n)