class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # BFS, min minutes is how many level to reach the bottom 
        
        queue = collections.deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        
        level = 0
        while queue:
            i,j,level = queue.popleft()
            
            if i<len(grid)-1 and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                queue.append((i+1,j,level+1))
            
            if i>0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                queue.append((i-1,j,level+1))
            
            if j<len(grid[0])-1 and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                queue.append((i,j+1,level+1))
            
            if j>0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                queue.append((i,j-1,level+1))
                
        # check if there are any remaining fresh orange 
        remain = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    remain = 1
        
        if remain == 1:
            return -1
        else:
            return level 

# Time: O(N), N is the size of grid
# Space:O(N)        
        
        