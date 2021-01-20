class Solution:
    def convert(self, s: str, numRows: int) -> str:
    

        # rows:  123 21  23  21
        # steps: 11 -1-1 11 -1-1 
        
        # rows:  1234 321 234
        # steps: 111 -1-1-1 111 -1-1-1
      
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
        
# Time: O(N)
# Space:O(N)        
        
        
        