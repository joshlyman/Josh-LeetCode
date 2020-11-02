# Refer solution
# https://leetcode.com/problems/range-sum-query-2d-immutable/solution/

# Approach #4 (Caching Smarter) [Accepted]

# Sum(ABCD)=Sum(OD)−Sum(OB)−Sum(OC)+Sum(OA)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix) 
        
        if m == 0: 
            return None
        
        n = len(matrix[0])
        
        if n == 0:
            return None 
        
        self.SumMatrix = [[0 for i in range(n+1) ] for j in range(m+1)]
        
        # pre compute to store 
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.SumMatrix[i][j] = self.SumMatrix[i][j-1]+ self.SumMatrix[i-1][j] - self.SumMatrix[i-1][j-1] + matrix[i-1][j-1]   
                    
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.SumMatrix[row2+1][col2+1] - self.SumMatrix[row2+1][col1] - self.SumMatrix[row1][col2+1] + self.SumMatrix[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Time: O(1) time per query, O(mn) time pre-computation. The pre-computation in the constructor takes O(mn)O(mn) time. Each sumRegion query takes O(1) time.
# Space: O(mn). The algorithm uses O(mn) space to store the cumulative region sum.