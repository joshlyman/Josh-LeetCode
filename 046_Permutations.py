class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # recursion       
        
        if len(nums)<=1:
            return [nums]
        
        res = []
       
        for i,num in enumerate(nums):
            
            # remaining numbers formulates new nums as param in permute 
            n = nums[:i]+nums[i+1:]
            
            for y in self.permute(n):
                res.append([num]+y)
                
        return res 

# V2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:    
    
    # DFS / Backtracking
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    
# Time: O(NxN!)
# Space: O(N!)