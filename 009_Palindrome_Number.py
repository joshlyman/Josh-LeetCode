class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num = 0 
        
        if x<0:
            False 
            
        a = abs(x)
        
        while (a!=0):
            temp = a % 10
            num = num*10 + temp
            a = int(a/10)
            
        if x == num:
            return True
        else:
            return False 


# Time: O(n)
# Space: O(1)