class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # need to consider low and upper element because res.append(str(nums[i]+1)) and we use range 2 (nums[i+1] - nums[i] == 2)
        # for example: [1], low = 0, upper = 100. 
        nums = [lower-1] + nums + [upper+1]
        res = []
        
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                res.append(str(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        
        return res

# Time: O(N)
# Space:O(N)