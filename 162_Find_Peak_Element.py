# linear scan
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return i-1
        return len(nums)-1

# Time: O(N)
# Space:O(1)


# Binary search 

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            
            # push mid to become peak where nums[mid]>mid[mid+1]
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        return left
            

# Time: O(logN)
# Space:O(1)