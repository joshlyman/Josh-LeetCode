The code below tracks two variables (a,b) representing the two highest values found in the array. After one linear pass, we can use these values to return the answer.


class Solution:
    def maxProduct(self, nums):
        a, b = float('-inf'), float('-inf')
        for x in nums:
            if x>a:
                a, b = x, a
            elif x>b:
                b = x
        return (a-1)*(b-1)

Time: O(N)
Space:O(1)

