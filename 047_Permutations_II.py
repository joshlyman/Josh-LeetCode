class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # DFS + backtracking: remove duplicates from candidates 
        res = []
        nums = sorted(nums)
        self.dfs(nums,[],res)
        return res 
        
    def dfs(self,nums,path,res):
        if len(nums)==0:
            res.append(path)
        
        for i in range(len(nums)):
            
            # need to remove duplicates here 
            if i>0 and nums[i] == nums[i-1]:
                continue 
            
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
        
        
        
# Time: O(NxN!)
# Space:O(N!)