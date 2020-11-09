# For each group, fill it with value index and remember it's size as area[index] = dfs(...).

# Then for each 0, look at the neighboring group ids seen and add the area of those groups, plus 1 for the 0 we are toggling. This gives us a candidate answer, and we take the maximum.

# To solve the issue of having potentially no 0, we take the maximum of the previously calculated areas.

# It is essentially a union-find method 

# 1.Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map.
# 2.Loop every cell == 0, check its connected islands and calculate total islands area.

def largestIsland(self, grid):
        N = len(grid)

        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, index):
            res = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res + 1

        # DFS every island and give it an index of island
        index = 2
        areas = {0: 0}
        for x in xrange(N):
            for y in xrange(N):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can connect
        res = max(areas.values())
        for x in xrange(N):
            for y in xrange(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y))
                    res = max(res, sum(areas[index] for index in possible) + 1)
        return res


# My solution
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        # 1.dfs each island to mark index and store area in dict 
        # 2.loop each 0 and get the max area after approaching four directions 
        
        n = len(grid)
        
        def move(x,y):
            for i,j in ((-1,0),(1,0),(0,1),(0,-1)):
                if 0<=x+i<n and 0<=y+j<n:
                    # not return, we need to use the generator to return 1 by 1
                    yield x+i,y+j
            
        def dfs(x,y,index):
            res = 0
            grid[x][y] = index
            for i,j in move(x,y):
                if grid[i][j] ==1:
                    res+=dfs(i,j,index)
            # because previous 1 needs to be count too 
            return res+1
            
        
        index = 2
        areas = {0:0}
        # 0 and 1 has been taken 
        
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    areas[index]=dfs(x,y,index)
                    index+=1
        
        # first of maxarea should be max value of current island 
        maxarea = max(areas.values())
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    possibleindex = set(grid[i][j] for i,j in move(x,y))
                    newsum = sum(areas[index] for index in possibleindex) +1
                    maxarea = max(maxarea,newsum)
        
        return maxarea 

# Time: O(N^2)
# Space:O(N^2)                   
                    
                    
                    

                    
                    
                    
                    
                    

