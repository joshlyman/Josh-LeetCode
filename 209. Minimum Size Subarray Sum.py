# Other similar sliding window 

# Count Number of Nice Subarrays
# Replace the Substring for Balanced String
# Max Consecutive Ones III
# Binary Subarrays With Sum
# Subarrays with K Different Integers
# Fruit Into Baskets
# Shortest Subarray with Sum at Least K


# Two Pointers 
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0
        
        total = left = 0
        result = len(nums)
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)

                # move left 
                total -= nums[left]
                left += 1
        
        return result if result <= len(nums) else 0

# Time: O(N)
# Space:O(1)


# Binary Search 

class Solution:

def minSubArrayLen(self, target, nums):
    result = len(nums) + 1
    for idx, n in enumerate(nums[1:], 1):
        nums[idx] = nums[idx - 1] + n
    left = 0
    for right, n in enumerate(nums):
        if n >= target:
            left = self.find_left(left, right, nums, target, n)
            result = min(result, right - left + 1)
    return result if result <= len(nums) else 0

def find_left(self, left, right, nums, target, n):
    while left < right:
        mid = (left + right) // 2
        if n - nums[mid] >= target:
            left = mid + 1
        else:
            right = mid
    return left

# Time: O(NlogN)
# Space:O(1)