# greedy:
# Pick the locally optimal move at each step, and that will lead to the globally optimal solution

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        
        local_max,global_max = 0,0 
        
        for num in nums:
            local_max = max(num+local_max,0)
            global_max = max(global_max,local_max)
            
        return global_max 

# Time: O(n)
# Space:O(1)

# DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i]+= nums[i-1]
            max_sum = max(nums[i],max_sum)
        
        return max_sum
        
# Time: O(n)
# Space:O(1)     
        
# sliding window
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        result = max(nums)
        i = 0
        
        temp = 0
        while i < len(nums):
            temp += nums[i]
            if temp < 0:
                temp = 0
                i += 1
            else:
                result = max(temp, result)
                i += 1
        
        return result
        
# Time: O(n)
# Space:O(1) 
