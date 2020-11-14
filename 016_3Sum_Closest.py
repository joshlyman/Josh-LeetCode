# 3Sum fixes one number and uses either the two pointers pattern or a hash set to find complementary pairs. Thus, the time complexity is O(N^2)

# Two Pointers 
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        
        for i in range(len(nums)):
            
            # set up two pointers 
            lo, hi = i+1,len(nums)-1
            
            while (lo<hi):
                
                sum = nums[i]+nums[lo]+nums[hi]
                
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                
                if sum < target:
                    lo+=1
                else:
                    hi-=1
            
            if diff == 0:
                break
            
        return target - diff 

# Time: O(N^2): O(NlogN + N^2) 
# Space:O(logN) to O(N)