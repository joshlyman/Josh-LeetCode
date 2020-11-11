class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        
        # if > 3: we need to return 3rd largest number, so remove first 2 largest number 
        nums -= {max(nums)}
        nums -= {max(nums)}
        
        return max(nums)

# Time: O(N), set operation takes O(N)
# Space:O(N)