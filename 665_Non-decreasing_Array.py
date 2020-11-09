class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # An array of 2 numbers can always be fixed up
        if len(nums) <= 2:
            return True

        count = 0
        idx = -1
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                if count:
                    # Only one outlier allowed
                    return False
                else:
                    count += 1
                    idx = i

        if not count:
            return True

        # If idx == 0, nums[0] can be dropped to fix the sequence
        # If idx == len(nums)-2, nums[len(nums)-1] can be dropped to fix the sequence
        if idx == 0 or idx == len(nums)-2:
            return True

        # Check if nums[idx] can be dropped to fix the sequence
        if nums[idx+1] >= nums[idx-1]:
            return True
        # Check if nums[idx+1] can be dropped to fix the sequence
        if nums[idx+2] >= nums[idx]:
            return True
        
        # No way to fix the sequence
        return False

# Time: O(N)
# Space:O(1)