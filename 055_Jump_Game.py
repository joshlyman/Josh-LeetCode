# Greedy: backwwards, find the leftmost node to compare

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # greedy
        # Iterating right-to-left, for each position we check if there is a potential jump that reaches a GOOD index 
        # (currPosition + nums[currPosition] >= leftmostGoodIndex). If we can reach a GOOD index, then our position is itself GOOD.
        lastgoodindx = len(nums)-1
        for i in reversed(range(len(nums))):
            if i+nums[i] >=lastgoodindx:
                lastgoodindx = i
        
        return lastgoodindx == 0

# Time: O(N)
# Space:O(1)

# DP with bottom up: forwards
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maxind = 0
        for i in range(len(nums)):
           
            #  if reaching to end or cannot reach in the middle, need to return False 
            if i > maxind:
                return False 
            
            maxind = max(maxind,i+nums[i])
           
            if maxind >=len(nums)-1:
                return True
        
        return False

# Time: O(N)
# Space:O(1)
