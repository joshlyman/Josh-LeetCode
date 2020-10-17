class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # [0,1] -> right 
        # [1,0] -> turn right,down 
        # [0,-1] -> turn right, left 
        # [-1,0] -> turn right, up 
        # [0,1] -> turn right, right 
        
        if not matrix:
            return []
        
        output = []
        
        n,m = len(matrix),len(matrix[0])
        dx = 0
        dy = 1
        num = m*n 
        
        x,y = 0,0
        
        while num:
            output.append(matrix[x][y])
            num -=1 
            matrix[x][y] = None
            
            if x+dx>n-1 or y+dy >m-1 or matrix[x+dx][y+dy] == None:
                dy,dx = -dx,dy
            
            x = x+dx
            y = y+dy 
                
                
                
        return output 

# Time: O(N), where N is the total number of elements in the input matrix. We add every element in the matrix to our final answer.

# Space:
# O(1) without considering the output array, since we don't use any additional data structures for our computations.
# O(N) if the output array is taken into account.