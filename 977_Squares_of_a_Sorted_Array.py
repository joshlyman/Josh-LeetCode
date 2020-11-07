# 1. sort 
class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)

# Time: O(NlogN)
# Space:O(N)


# 2. Two Pointer

# Since the array A is sorted, loosely speaking it has some negative elements with squares in decreasing order, then 
# some non-negative elements with squares in increasing order.

# For example, with [-3, -2, -1, 4, 5, 6], we have the negative part [-3, -2, -1] with squares [9, 4, 1], 
# and the positive part [4, 5, 6] with squares [16, 25, 36]. Our strategy is to iterate over the negative part 
# in reverse, and the positive part in the forward direction.

# We can use two pointers to read the positive and negative parts of the array - one pointer j in the positive direction, 
# and another i in the negative direction.

# Now that we are reading two increasing arrays (the squares of the elements), we can merge these arrays together using a 
# two-pointer technique.

class Solution(object):
    def sortedSquares(self, A):
		N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans 

# Time: O(N)
# Space:O(1)



        return ans