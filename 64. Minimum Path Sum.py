# DP 2D 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

# Time: O(NM)
# Space:O(1)


# DP 1D 
def minPathSum(self, grid):
        M, N = len(grid), len(grid[0]) 
        dp = [0] + [sys.maxint] * (N-1)
        for i in range(M):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, N):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[-1]

# Time: O(NM)
# Space:O(1)
