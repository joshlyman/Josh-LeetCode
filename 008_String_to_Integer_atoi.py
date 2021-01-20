class Solution:
    def myAtoi(self, s: str) -> int:
        ###better to do strip before sanity check (although 8ms slower):
        # remove all empty strings to remain the real letters or numbers in strings 
        
        ls = list(s.strip())
        
        if len(ls) == 0:
            return 0
          
        sign = 0
        if ls[0] == '-':
            sign = -1
            del ls[0]
        elif ls[0] == '+':
            sign = 1
            del ls[0]
        else:
            sign = 1
            
            
        ret = 0
        i = 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret*10 + ord(ls[i]) - ord('0')
            i+=1
        
        # make sure number is in 32-bit signed integer range: [−2^31,  2^31 − 1].
        if sign == 1:
            return min(sign*ret,2**31-1)
        elif sign == -1: 
            return max(sign*ret,-2**31)

# Time: O(n)
# Space:O(1)         
        
        