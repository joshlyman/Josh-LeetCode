class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s 
        
        zigzag = ['' for i in range(numRows)]
        
        row = 0
        step = 1
        
        for si in s:
            zigzag[row]+=si
            
            if row == 0:
                step = 1
            elif row == numRows -1:
                step = -1
            
            row+=step
        
        return ''.join(zigzag)
        
Time: O(N)
Space:O(N)        
        
        
        