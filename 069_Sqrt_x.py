# Approach 1
class Solution:
    def mySqrt(self, x: int) -> int:
        
        from math import e, log
        
        # e^(1/2)log(x)
        if x<2:
            return x
        
        # a^2 <=x< (a+1)^2
        left = int(e**(0.5*log(x)))
        right = left +1
        
        if right*right >x:
            return left
        else:
            return right 

# Time: O(1)
# Space:O(1)

# Approach 2 Binary Search 
# Let's go back to the interview context. For x≥2 the square root is always smaller than x/2 and larger than 0 : 0 < a < x/2.
# Since a is an integer, the problem goes down to the iteration over the sorted set of integer numbers. Here the binary search enters the scene.

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
            
        return right

# Time: O(logN)
# Space:O(1)


# Approach 3: Recursion + Bit Shifts
# Refer from:
# https://leetcode.com/problems/sqrtx/solution/

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = self.mySqrt(x >> 2) << 1
        right = left + 1
        return left if right * right > x else right
# Time: O(logN)
# Space:O(logN)



# Approach 4: Newton's Method

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2        
            
        return int(x1)
# Time: O(logN)
# Space:O(1)


