class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge cases:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        
        # DP - decide each problem by its sub-problems:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        
        return dp[-1]
            
  
Time: O(n)
Space:O(n)


        # DP with space O(1)
        
#         last, now = 0,0
        
#         for i in nums:
#             last,now = now,max(last+i,now)
            
#         return now 
            
# Time: O(n)
# Space:O(1)
