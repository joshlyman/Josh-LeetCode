# Brute force 

# offical solution
# 1.Implement missing(idx) function that returns how many numbers are missing until array element with index idx. Function returns nums[idx] - nums[0] - idx.
# 2.Find an index such that missing(idx - 1) < k <= missing(idx) by a linear search.
# 3.Return kth smallest nums[idx - 1] + k - missing(idx - 1).

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx
                
        n = len(nums)
        # If kth missing number is larger than 
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1) 

        idx = 1
        # find idx such that 
        # missing(idx - 1) < k <= missing(idx)
        while missing(idx) < k:
            idx += 1

        # kth missing number is greater than nums[idx - 1]
        # and less than nums[idx]
        return nums[idx - 1] + k - missing(idx - 1)

# Time: O(N)
# Space:O(1)

# one pass
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
       
        for i in range(1,len(nums)):
            # missing number between nums[i-1] and nums[i]
            diff = nums[i]-nums[i-1]-1
            
            if diff >=k:
                return nums[i-1]+k
            k-=diff
        
        return nums[len(nums)-1]+k


# Time: O(N)
# Space:O(1)




# Binary Search: reduce time from O(N) to O(logN)
# The idea is to find the leftmost element such that the number of missing numbers until this element is less or equal to k.

# offical solution
# Implement missing(idx) function that returns how many numbers are missing until array element with index idx. Function returns nums[idx] - nums[0] - idx.
# Find an index such that missing(idx - 1) < k <= missing(idx) by a binary search.
# Return kth smallest nums[idx - 1] + k - missing(idx - 1).

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx
            
        n = len(nums)
        # If kth missing number is larger than 
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1) 
        
        left, right = 0, n - 1
        # find left = right index such that 
        # missing(left - 1) < k <= missing(left)
        while left != right:
            pivot = left + (right - left) // 2
            
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot 
        
        # kth missing number is greater than nums[left - 1]
        # and less than nums[left]
        return nums[left - 1] + k - missing(left - 1) 

# Time: O(logN), since it's a binary search algorithm in the worst case when the missing number is less than the last element of the array.
# Space:O(1)

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0
        
        diff = nums[-1] - nums[0] + 1 # complete length
        missing = diff - len(nums) # complete length - real length
        if k > missing: # if k is larger than the number of mssing words in sequence
            return nums[-1] + k - missing
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2

            # nums[mid] - nums[left] is expected distance between nums[mid] and nums[left]
            # mid - left is real distance between index of mid and left 
            missing = nums[mid] - nums[left] - (mid - left)
            if missing < k:
                left = mid
                k -= missing # KEY: move left forward, we need to minus the missing words of this range
            else:
                right = mid
                
        return nums[left] + k # k should be between left and right index in the end

# Time: O(logN), since it's a binary search algorithm in the worst case when the missing number is less than the last element of the array.
# Space:O(1)















