class Solution:
    def convertToTitle(self, n: int) -> str:
        column = []
        while n > 0:
            
            # # number is the int part, output is 
            # number, output = divmod(number-1, 26)
            
            # number should start from 0, so number - 1, it means 0+'A' 
            div = (n-1)//26
            output = (n-1)%26
            n = div 
            
            # 28 will be: ['1','0'] so need to reverse later 
            column.append(output)
            
            
        # start from 'A' to transfer each number to chr 
        return ''.join([chr(i+ord('A')) for i in reversed(column)])

# Time: O(N)
# Space:O(N)