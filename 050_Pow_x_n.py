https://leetcode.com/problems/powx-n/discuss/182026/Python-or-Recursion-tm

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # recursive
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
        
# Time: O(logN)
# Space:O(logN)



class Solution:
    def myPow(self, x: float, n: int) -> float:        
        # iterative  
        #Deal with negative power:
        if n < 0: 
            x = 1/x
            n = -n
            
        #Iterate:
        res = 1
        while n:
            if n % 2:
                res = res*x
            x = x*x 
            n = n//2
            
        return res

# Time: O(logN)
# Space:O(1)