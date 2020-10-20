
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1. DFS
        # Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Depth First Search. During DFS, every visited node should be set as '0' to mark as visited node. Count the number of root nodes that trigger DFS, this number would be the number of islands since each DFS starting at some root identifies an island.
        if not grid: 
            return 0
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =='1':
                    self.dfs(grid,i,j)
                    count+=1
        
        return count 
    
    
    def dfs(self,grid,i,j):
        if i<0 or j <0 or i>=len(grid) or j >=len(grid[0]) or grid[i][j]!='1':
            return 
        
        # remove this node
        grid[i][j] = '#'
        
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        
# Time: O(MxN)
# Space:O(MxN) in worst cases that grid map is filled with lands 
        
        # 2. BFS 
        # Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search. Put it into a queue and set its value as '0' to mark as visited node. Iteratively search the neighbors of enqueued nodes until the queue becomes empty.
        
        # DFS and BFS difference is BFS linearly seach neighbours and DFS recursively search each node's neighbords, time: O(MxN) space is O(min(M,N)) 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        
        
        from collections import deque 
        queue = deque([])
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    queue.append((i,j))
                    count += 1
                    self.helper(grid,queue) # turn the adjancent '1' to '0'
                    
        print(grid)
        return count
    
    def helper(self,grid,queue):
        while queue:
            I,J = queue.popleft()
            for i,j in [I-1,J],[I+1,J],[I,J-1],[I,J+1]:
                if 0<= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    queue.append((i,j))
                    grid[i][j] = 0 #0
       

# Time:  O(MxN) 
# Space: O(min(M,N)) https://imgur.com/gallery/M58OKvB    
        
        # 3.Union find (or disjoint set) 
        # Traverse the 2d grid map and union adjacent lands horizontally or vertically, at the end, return the number of connected components maintained in the UnionFind data structure.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if len(grid) == 0: 
        	return 0
        
        row = len(grid)
        col = len(grid[0])
        
        self.count = sum(grid[i][j]=='1' for i in range(row) for j in range(col))
        parent = [i for i in range(row*col)]
        
        def find(x):
            if parent[x]!= x:
                return find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot, yroot = find(x),find(y)
            if xroot == yroot: return 
            parent[xroot] = yroot
            self.count -= 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i*col + j
                if j < col-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < row-1 and grid[i+1][j] == '1':
                    union(index, index+col)
        return self.count
        
# Time: O(MxN)
# Space:O(MxN)

# other DFS and BFS solutions from https://leetcode.com/problems/number-of-islands/discuss/345981/Python3Number-of-Islands-BFS-%2B-DFS