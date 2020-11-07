# Offical Solution:
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/

# Heap 

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        vals = [val for row in matrix for val in row]
        heapq.heapify(vals)
        for _ in range(k):
            ans = heapq.heappop(vals)
        return ans

# Time: O(N^2)

# Heapify: O(nn)
# k times pop : O(k log(n2)) which becomes O(klogn)
# Therefore time complexity is: O(n*n)

# Space:O(N^2)

# Binary Search 

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        # Count all the numbers smaller than or equal to middle in the matrix. 
        # As the matrix is sorted, we can do this in O(N). Note that this is determining 
        # the size of the left-half of the array.
        def findOrd(matrix, val):
            order = 0
            for row in matrix:
                for col in row:
                    if col <= val: 
                    	order += 1
            return order
        
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            order = findOrd(matrix, mid)
            
            # means kth smallest element should be in the left, so we shrink the range by make mid as right 
            if order >= k:
                r = mid
            else:
                l = mid + 1
        return l

# Time: O(Nlog(Max-Min))
# Space: O(1)


# Sorting 
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:        
        res = []
        for r in matrix:
            res += r
        return sorted(res)[k-1]
