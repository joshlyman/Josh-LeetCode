# Take K as a carry.
# Add it to the lowest digit,
# Update carry K,
# and keep going to higher digit.

for i in range(len(A) - 1, -1, -1):
            K, A[i] = divmod(A[i] + K, 10)
        return [int(i) for i in str(K)] + A if K else A

# Time: O(N)
# Space:O(1)

# mine 
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1]+=K
        for i in range(len(A) - 1, -1, -1):
            carry= A[i]//10
            A[i] = A[i]%10
            
            if i>0:
                A[i-1]+= carry
            
        if carry:
            return [int(i) for i in str(carry)]+A
        else:
            return A     

# Time: O(N)
# Space:O(1)


# V2
class Solution(object):
    def addToArrayForm(self, A, K):
        A[-1] += K
        for i in xrange(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = map(int, str(carry)) + A
        return A
