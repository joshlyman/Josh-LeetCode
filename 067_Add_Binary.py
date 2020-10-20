class Solution:
    def addBinary(self, a: str, b: str) -> str:
         # can covert str to int but this will not work when string is very long and takes very long time. O(N+M)
        # 1.use bit by bit computation to speed up, O(max(N,M)), space is O(max(N,M)) 
        
        if a == "0":
            return b
        
        if b == "0":
            return a
        
        carry = 0
        result = ''
        
        a = list(a)
        b = list(b)
    
        while a or b or carry:
            if a:
                carry += int(a.pop()) 
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]

# Time: O(max(N,M))
# Space O(max(N,M)) 
        

# 2.use bit manipulation if not allowed to use addition 
# answers w/o carry is x^y, carry is x&y <<1, shift 1 bit to left 
# answers as new x, carry as new y, do loop 
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # convert them to integer 
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        
        # return x as binary form 
        return bin(x)[2:]

# Time: O(N+M)
# Space O(max(N,M))     
        
        
        
        
        
        
        
        