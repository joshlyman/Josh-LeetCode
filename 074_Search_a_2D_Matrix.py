class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        
        if m == 0:
            return False 
        
        n = len(matrix[0])
        
        left,right = 0, m*n-1
        
        while left <= right:
            
            pivotidx = (left+right)//2
            row = pivotidx // n
            col = pivotidx % n
            
            pivot = matrix[row][col]
            
            if pivot == target:
                return True
            else:
                if target < pivot:
                    right = pivotidx - 1
                else:
                    left = pivotidx + 1    
            
        return False

# Time: O(logmn) since it is a standard binary search
# Space:O(1)