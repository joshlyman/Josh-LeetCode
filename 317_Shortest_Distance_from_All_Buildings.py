# BFS
# normallu use BFS to find shortest path 

# Use hit to record how many times a 0 grid has been reached and use distSum to record the sum of distance 
# from all 1 grids to this 0 grid. A powerful pruning is that during the BFS we use count1 to count 
# how many 1 grids we reached. If count1 < buildings then we know not all 1 grids are connected are 
# we can return -1 immediately, which greatly improved speed (beat 100% submissions).

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: 
            return -1
        M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
        hit, distSum = [[0] * N for i in range(M)], [[0] * N for i in range(M)]

        def BFS(start_x, start_y):
            visited = [[False] * N for k in range(M)]
            visited[start_x][start_y], count1, queue = True, 1, collections.deque([(start_x, start_y, 0)])
            while queue:
                x, y, dist = queue.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]:
                            queue.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:
                            count1 += 1
            return count1 == buildings  
    
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    if not BFS(x, y): return -1
        return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])

# Time: O(MNK), K is the number od 1s in the grid 
# we are visiting the entire grid (in the worst case) starting from each '1'

# Space:O(2MN)
# one for finding buildings (which is no. of 1's) and second for the iteration where we call BFS.


# Much more clear version 
# Other Solution:
# BFS V2
def shortestDistance(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    if m: n = len(grid[0])
    if not m or not n:
        return -1
    dist = [[0]*n for i in range(m)]
    totalB = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1: totalB+=1
    ## do BFS from each building, and decrement all empty place for every building visit
    ## when grid[i][j] == -totalB, it means that grid[i][j] are already visited from all buildings
    ## and use dist to record distances from buildings
    def bfs(i, j, bIndex):
        queue = collections.deque([(i, j, 0)])
        while queue:
            i, j, d = queue.popleft()
            for x,y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if 0<=x<m and 0<=y<n and grid[x][y]==bIndex:
                    dist[x][y] += d+1
                    grid[x][y] -= 1
                    queue.append((x, y, d+1))
    
    bIndex = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                bfs(i, j, bIndex)
                bIndex -= 1
    res = [dist[i][j] for i in range(m) for j in range(n) if grid[i][j]+totalB==0]
    return min(res) if res else -1


