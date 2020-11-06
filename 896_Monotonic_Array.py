class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # two pass 
        # check adjacent elements 
        
        return all(A[i]<=A[i+1] for i in range(len(A)-1)) or all(A[i]>=A[i+1] for i in range(len(A)-1))

# Time: O(N)
# Space:O(1)


# One pass 
class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = True

        for i in xrange(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing

# Time: O(N)
# Space:O(1)
