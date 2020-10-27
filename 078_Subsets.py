
# recursion
def subsets(self, nums):
        ret = []
        self.dfs(nums, [], ret)
        return ret
    
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], ret)


# iterative
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res = [[]]
        
        for num in nums:
                res+=[curr+[num] for curr in res]
        
        return res 




Time: O(Nx2^N)
Space:O(Nx2^N)
