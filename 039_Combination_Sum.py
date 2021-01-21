# Backtracking 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = []
        
        def backtrack(remain,comb,start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return 
            
            # not satify condition 
            elif remain <0:
                # exceed the scope, stop exploration.
                return 
            
            for i in range(start,len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain-candidates[i],comb,i)
                # backtrack, remove the number from the combination
                comb.pop()
        
        backtrack(target,[],0)
        
        return results 


# Refer from 
# https://leetcode.com/problems/combination-sum/solution/

# Time: O(N^(T/M)+1)
# Let N be the number of candidates, T be the target value, and M be the minimal value among the candidates.


# Space:O(T/M)

# V2
class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):

            # Here we have to use concatenation because if we use append, then path will be passed by 
            # reference and it will cause allocation problem
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)

# V3
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        self.backtrack(0,candidates,target,[],res)
        return res 
        
    
    def backtrack(self,start,candidates,target,path,res):
        if target <0:
            return 
        
        if target ==0:
            res.append(path)
            return 
        
        for i in range(start,len(candidates)):
            self.backtrack(i,candidates,target-candidates[i],path+[candidates[i]],res)
        
        
        




