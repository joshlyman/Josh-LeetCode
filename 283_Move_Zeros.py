class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        pos = 0
        
        while left <= len(nums) -1:
            if nums[left] !=0:
                nums[pos] = nums[left]
                pos +=1
            left +=1
            
        while pos <= len(nums)-1:
            nums[pos] = 0
            pos +=1
        
        
            

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos] = nums[i]
                pos+=1
        
        for i in range(pos,len(nums)):
            nums[i]= 0 

# Time: O(n)
# Space: O(1)
