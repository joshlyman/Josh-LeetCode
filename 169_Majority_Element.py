# Hashmap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Hashmap
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# Time: O(N)
# Space:O(N)


# simply sorting
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

# Time: O(NlogN)
# Space:O(1)

# Radnomization
import random

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
# Time: O(N) or O(infinity)
# Space：O(1)

# Divide and Conquer
class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)

# Time: O(NlogN)
# Space:O(logN)

# Boyer-Moore Voting Algorithm
# https://zh.wikipedia.org/wiki/%E5%A4%9A%E6%95%B0%E6%8A%95%E7%A5%A8%E7%AE%97%E6%B3%95

# If we had some way of counting instances of the majority element as +1 and instances of any other element as −1, 
# summing them would make it obvious that the majority element is indeed the majority element.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate

# Time: O(N)
# Space:O(1)



