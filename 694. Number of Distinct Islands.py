# https://leetcode.com/problems/number-of-distinct-islands/discuss/108480/Simple-Python-169ms

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        island_shapes = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j, positions, rel_pos):
            grid[i][j] = -1
            for direction in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                next_i, next_j = i + direction[0], j + direction[1]
                if (0 <= next_i < rows and 0 <= next_j < cols) and grid[next_i][next_j] == 1:
                    new_rel_pos = (rel_pos[0] + direction[0], rel_pos[1] + direction[1])
                    positions.append(new_rel_pos)
                    dfs(next_i, next_j, positions, new_rel_pos)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    positions = []
                    dfs(i, j, positions, (0, 0))
                    island_shapes.add(tuple(positions))
        return len(island_shapes)


# V2: my version for DFS 
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.distIslands = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1:
                    
                    # initlize the list of relative positions 
                    positions = []

                    # (0,0) is the start point of relative position 
                    self.dfs(i,j,grid,positions,(0,0))
                    self.distIslands.add(tuple(positions))
        
        return len(self.distIslands)
    
    # need to find the islands and return the relative positions 
    def dfs(self,i,j,grid,positions,relat_pos):
        if i<0 or j <0 or i>=len(grid) or j >=len(grid[0]) or grid[i][j]!=1:
            return 
        
        grid[i][j] = -1
        positions.append(relat_pos)
        
        self.dfs(i+1,j,grid,positions,(relat_pos[0]+1,relat_pos[1]))
        self.dfs(i-1,j,grid,positions,(relat_pos[0]-1,relat_pos[1]))
        self.dfs(i,j+1,grid,positions,(relat_pos[0],relat_pos[1]+1))
        self.dfs(i,j-1,grid,positions,(relat_pos[0],relat_pos[1]-1))
        

Time: O(NxN)
Space:O(NxN)
