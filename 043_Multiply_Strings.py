class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res1, res2 = 0, 0 
        for d in num1:
            
            # we cannot use int here, but we can use ord 
            res1 = res1 * 10 + (ord(d) - ord('0'))
        for d in num2:
            res2 = res2 * 10 + (ord(d) - ord('0'))
        return str(res1 * res2)

# Time: O(N)
# Space:O(1)