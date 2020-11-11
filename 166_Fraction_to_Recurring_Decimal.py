class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, remainder = divmod(abs(numerator), abs(denominator))
        
        # if both negative, then * can remove the negative sign
        # if still negative, means one of them is negative and cannot be removed 
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        stack = []
        # store remainder and keep remainder times 10 until the remainder in stack is repeated 
        # (0,4) = divmod(4,333)
        # (0,40) = divmod(40,333)
        # (1,67) = divmod(400,333)
        # (2,4) = divmod(670,333)
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))
        
        # or use dict instead of stack 
        # remainder here is repeated first one 
        idx = stack.index(remainder)
        # after 0. to insert into 3rd position
        result.insert(idx+2, '(')
        result.append(')')
        
        # remove .(0) after integer if it is only integer 
        return ''.join(result).replace('(0)', '').rstrip('.')

# Time: O(N)
# Space:O(N)