# built in
def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    return bin(n).count('1')


# Using bit operation to cancel a 1 in each round
# Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000 
# which is just remove the last significant 1

def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        while n>0:
            if n%2==1:
                ans+=1
            n=n//2
        return ans

# Time: O(1)
# Space:O(1)

# use bit manipulation 
def hammingWeight(self, n: int) -> int:
    out = 0
    while n > 0:

    	# n & 1 means n%2
        if n & 1:
            out += 1

        # n>>=1 means n//2
        n >>= 1
    return out
