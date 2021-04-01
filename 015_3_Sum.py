class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            self.find_two_sums(nums,i+1, len(nums)-1, -nums[i], results)
            
        return results 
    
    
    def find_two_sums(self,nums,left,right, target, results):
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([-target, nums[left], nums[right]])
                right -=1
                left +=1
                while left < right and nums[left] == nums[left-1]:
                    left +=1
                while left < right and nums[right] == nums[right+1]:
                    right -=1
                
            elif nums[left] + nums[right] > target:
                right -=1
            else:
                left +=1
                
# Time: O(n^2): O(n^2) + Sorting: O(nlogn)
# Space: O(n): possible O(logn)
           
                
        


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


# V2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue 
            l,r = i+1,n-1
            
            while l<r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif temp>0:
                    r-=1
                else:
                    l+=1
        return ans 
                
        