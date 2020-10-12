class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first sort arrays then use 2 Sum II 2 pointers or 2 Sum hash table to do   
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            # first element must be started from 0 or cannot be euqal to previous element because it will give same result
            if i == 0 or nums[i-1]!= nums[i]:
                self.twoSumII(nums,i,res)
        
        return res 
    
    # repeat 2 Sum or 2 Sum II solution here
    def twoSumII(self,nums:List[int],i:int,res:List[List[int]]):
        low , high = i+1,len(nums)-1
        
        while low < high:
            sum = nums[i] + nums[low] + nums[high]
            
            if sum<0:
                low+=1
            elif sum >0:
                high-=1
            else:
                res.append([nums[i],nums[low],nums[high]])
                
                # continue 
                low +=1
                high -=1
                
                # avoid duplicate set 
                while low < high and nums[low] == nums[low-1]:
                    low+=1
                
            
# Time: O(n^2): O(n^2) + Sorting: O(nlogn)
# Space: O(n): possible O(logn)
