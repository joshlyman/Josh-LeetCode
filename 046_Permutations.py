class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        # 1. path, 2. used 3. candidates 4.results 
        results = []
        
        # can use hashtable to replace set 
        used = set()
        path = []
        
        self.dfs(path,used,nums,results)
        
        return results
        
    
    def dfs(self,path,used,nums,results):
        if len(path) == len(nums):
            results.append(list(path))
            return 
        
        for num in nums:
            # check if visited before: prunning 
            if num in used:
                continue 
            
            path.append(num)
            used.add(num)
            self.dfs(path,used,nums,results)
            
            # recover
            used.remove(num)
            path.pop()

# https://www.jiuzhang.com/problem/permutations/ 

# time: O(sum_m=1_n (P_N_M))

# 对于每一位，可以从n个元素中选择k个来放置，共有n位。  

# space: O(N!)

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