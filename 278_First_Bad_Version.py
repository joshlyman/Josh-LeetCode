# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # use linear scan will take O(n) time, instead using binary search will only take O(logn) time.
        left = 0
        right = n-1
        
        while (left <=right):
            
            # use (right + left)/2 might overflow
            # can use mid = int(left + (right-left)/2) or //2
            # use //2 will speed up because int takes time 
            mid = left + (right-left)//2
            if isBadVersion(mid):
                right = mid-1
            else:
                left = mid+1
            
        return left 
        
        
# Time: O(logn)
# Space:O(1)
        
        