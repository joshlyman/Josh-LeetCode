# https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation


# the same count appears mean they have same equal number of 0 and 1, so we need to store previous index of this count
# and get the length between previous index and current index, which is current max length of subarray 

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length=0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index
        
        return max_length

# Time: O(N)
# Space:O(N)