class Solution(object):
    def toHex(self, num):

        if num == 0:
            return '0'
        if num < 0:
            num = 2**32+num
            
        c = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        res = ''
        while num != 0:
            r = num % 16
            if r > 9:
                res+=(c[num % 16])
            else :
                res+=(str(r))
            num //= 16  
        return res[::-1] 

# Time: O(N)
# Space:O(1)

# V2
class Solution:
    def toHex(self, num: int) -> str:
        temp = num
        # ord('0') is 48, ord('a') is 97
        digit = ord('0')
        letter = ord('a')
        
        # for negative number, starts from ffffffff
        if temp < 0:
            temp += 2 ** 32
        elif temp == 0:
            return "0"

        result = []
        while temp != 0:
            # for 26, remainder = 10, which is a 
            remainder = temp % 16
            # for 26, temp = 1
            temp //= 16
            
            # chr: transfer integer to char (ASCII char)
            # 49 - 57: 1 - 9 
            if remainder < 10: 
                newHexChar = chr(digit+remainder) 
            # a - f : 10 - 15
            else:
                newHexChar = chr(letter+remainder-10) 
                
            result.append(newHexChar)
        # 26 will output ['a','1'], so need to reverse 
        result.reverse()
        
        return ''.join(result)


# Time: O(N)
# Space:O(1)
   
   