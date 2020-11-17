# Push the index on the stack. If the current number b is bigger than the last number a in the stack(found by index), 
# then we find the next great element for a. Process it twice as it is a circular array to make sure that we 
# can reread the next greater element after every element.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
    
        l = len(nums)
        # search two rounds in a circle 
        nums = nums * 2
        stack = []
        
        # use -1 to initilize because if no found, return -1
        res = [-1] * len(nums)
        
        for idx, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                res[stack.pop()] = num
            stack.append(idx)
        
        # only get first length of nums elements
        return res[:l]

# Time: O(N)
# Space:O(N)
