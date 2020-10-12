class Solution:
    def climbStairs(self, n: int) -> int:
        
        # use Fibonacci series to solve 
        prev, current = 0,1
        for i in range(n):
            prev,current = current,prev+ current
        return current
        
# Time: O(n)
# Space:O(1)

# if using DP, then 

# Time: O(n)
# Space:O(n)

# so Fib series reduce the space from DP 
