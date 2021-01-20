# https://leetcode.com/problems/next-permutation/discuss/545263/Python-3-Easy-to-understand

# 1　　2　　7　　4　　3　　1   find 2 -> first element which is smaller that next element 

# 1　　2　　7　　4　　3　　1   find 3 -> smallest emlement which is larget that 2

# 1　　3　　7　　4　　2　　1   swap 2 and 3

# 1　　3　　[1　　2　　4　　7]   sort nums after 3


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        
        # from end to begining, find the earliest decreasing number, this number is in i-1, so k = i-1, kth number 
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # nums are in descending order, has reached to the begining 
        if i == 0:   
            nums.reverse()
            return 
        
        # find the last ascending number, this number is in jth 
        k = i - 1    
        while nums[j] <= nums[k]:
            j -= 1
        
        # reverse these 2 numbers 
        nums[k], nums[j] = nums[j], nums[k]  
        
        # reverse the second part (from end to the first number, center is the second number)
        l, r = k+1, len(nums)-1  
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 
            r -= 1

# refer from https://leetcode.com/problems/next-permutation/solution/

# Note: 
# First of all, the requirements of in-place replacement and constant space should immediately indicate swapping (this goes for other questions too). 
# Secondly, it should be obvious that if the elements are increasing from the right, they are currently at their largest possible permutation, 
# so nothing can be done. I think the tricky part is simply knowing where to swap and reversing the last digits.   


# Time: O(N): two pass 
# Space:O(1): in-place modify, so it hints swap order 