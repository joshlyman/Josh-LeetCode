# Binary search row and col 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m = len(matrix) 
        n = len(matrix[0])
        
        rowpt = 0
        colpt = n - 1
        
        while rowpt<=m-1 and colpt>=0:
            if matrix[rowpt][colpt] == target:
                return True 
            elif matrix[rowpt][colpt] < target:
                rowpt +=1
            else:
                colpt -=1
        
        # print (matrix[rowpt][colpt])
        return False 

# Time: O(N+M)
# Space:O(1)

# or can do rowpt start from m-1 and colpt start from 0 