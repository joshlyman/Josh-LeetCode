''' Make a table to keep track of maximum form each node. Apply 
dfs on each node and collect the max length from all four sides. Increment + 1 
while returning and store in the table so that next time it will directly fetch 
the value from the table'''


class Solution:
     def __init__(self):
        self.max_len = 0
        self.table = {}
    
     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
       
        def dfs(x, y, prev):
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] <= prev: 
                return 0

            if (x,y) in self.table: 
                return self.table[(x,y)]

            path = 1 + max(dfs(x+1, y, matrix[x][y]), dfs(x-1, y, matrix[x][y]), dfs(x, y+1, matrix[x][y]), dfs(x, y-1, matrix[x][y]))

            self.max_len = max(self.max_len, path)
            self.table[(x,y)] = path
            return path

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                # set up a very small number before (0,0)
                dfs(i, j, -10000)

        return self.max_len

# Time: O(MN)
# Space:O(MN)