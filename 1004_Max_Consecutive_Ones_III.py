# The problem has asked for longest contiguous subarray that contains only 1s. What makes this problem a little trickier 
# is the K flips allowed from 0 --> 1. This means a contiguous subarray of 1's might not just contain 1's but also 
# may contain some 0's. The number of 0's allowed in a given subarray is given by K.

# In any sliding window based problem we have two pointers. One right pointer whose job is to expand the current window 
# and then we have the left pointer whose job is to contract a given window. At any point in time only one of these pointers 
# move and the other one remains fixed.

# The solution is pretty intuitive. We keep expanding the window by moving the right pointer. When the window has reached the limit 
# of 0's allowed, we contract (if possible) and save the longest window till now.


# Approach:

# Initialize two pointers. The two pointers help us to mark the left and right end of the window/subarray with contiguous 1's.

# left = 0, right = 0, window_size = 0

# We use the right pointer to expand the window until the window/subarray is desirable. i.e. number of 0's in the window are in the allowed range of [0, K].

# Once we have a window which has more than the allowed number of 0's, we can move the left pointer ahead one by one until we encounter 0 on the left too. This step ensures we are throwing out the extra zero.

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        
        # use right pointer to expand the window
        for right in range(len(A)):
            # if meeting 0, then continue 
            if A[right] == 0:
                K-=1
            
            # if more than # of allowed 0s, move left pointer ahead and add 1 back if A[left] is 0, if A[left] is 1, then keep moving 
            if K<0:
                K+= 1-A[left]
                left+=1
        
        # window size 
        return right-left+1
        
            
# Time: O(N)
# Space:O(1)