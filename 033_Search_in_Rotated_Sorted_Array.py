class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1 
        while begin <= end:
            mid = (begin + end)//2
            if nums[mid] == target:
                return mid

            # 4567012: mid:7,target:5,  
            # 4560123: mid:0,target:5
            if nums[mid] > nums[end]: # Left side of mid is sorted
                if  nums[begin] <= target and target < nums[mid]: # Target in the left side
                    end = mid - 1
                else: # in right side
                    begin = mid + 1
            else: # Right side is sorted
                if  nums[mid] < target and target <= nums[end]: # Target in the right side
                    begin = mid + 1
                else: # in left side
                    end = mid - 1
        return -1

# Time: O(logN)
# Space:O(1)