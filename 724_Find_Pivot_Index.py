# get prefix sum for left and right and see when they are equal 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1

#Time: O(N)
#Space:O(1)