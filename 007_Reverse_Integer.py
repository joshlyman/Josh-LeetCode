class Solution:
    def reverse(self, x: int) -> int:
        
        num = 0
        a = abs(x)
        
        while (a!=0):
            temp = a %10
            num = num*10+temp
            a = int(a/10)
            # print(a)
            # print(num)
            
        
        if x > 0 and num < 2147483647:
            return num 
        elif x < 0 and num<=2147483647:
            return -num 
        else:
            return 0 

# Time: O(n)
# Space: O(n)