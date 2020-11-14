# Refer from:
# https://leetcode.com/problems/longest-common-subsequence/discuss/436719/Python-very-detailed-solution-with-explanation-and-walkthrough-step-by-step.

# 1. Recursion 

class Solution:
        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            return self.helper(text1, text2, 0, 0)
            
        def helper(self, text1, text2, i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + self.helper(text1, text2, i + 1, j + 1)
            else:
                return max(self.helper(text1, text2, i+1, j), self.helper(text1, text2, i, j + 1))


						lcs("AXYT", "AYZX")
                           /              \
             lcs("AXY", "AYZX")            lcs("AXYT", "AYZ")
             /        \                      /              \ 
    lcs("AX", "AYZX") lcs("AXY", "AYZ")   lcs("AXY", "AYZ") lcs("AXYT", "AY")

# Time: O(MN^2)
# Space:O(MN)

# 2. Recursion with Memoization

class Solution:
        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            m = len(text1)
            n = len(text2)
            memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
            return self.helper(text1, text2, 0, 0, memo)
    
        def helper(self, text1, text2, i, j, memo):
            if memo[i][j] < 0:
                if i == len(text1) or j == len(text2):
                    memo[i][j] = 0
                elif text1[i] == text2[j]:
                    memo[i][j] = 1 + self.helper(text1, text2, i + 1, j + 1, memo)
                else:
                    memo[i][j] = max(
                        self.helper(text1, text2, i + 1, j, memo),
                        self.helper(text1, text2, i, j + 1, memo),
                    )
            return memo[i][j]

# Time: O(MN)
# Space:O(MN)

# 3. Bottom Up DP
class Solution:
        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            m = len(text1)
            n = len(text2)
            memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
            for row in range(1, m + 1):
                for col in range(1, n + 1):
                    if text1[row - 1] == text2[col - 1]:
                        memo[row][col] = 1 + memo[row - 1][col - 1]
                    else:
                        memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])
    
            return memo[m][n]

# Time: O(MN)
# Space:O(MN)

# 4. DP with Reduced space complexity
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        if m < n:
            return self.longestCommonSubsequence(text2, text1)

        # instead of using m and n for 2D array, use 1D array n to represent DP space
        memo = [[0 for _ in range(n + 1)] for _ in range(2)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    memo[1 - i % 2][j + 1] = 1 + memo[i % 2][j]
                else:
                    memo[1 - i % 2][j + 1] = max(memo[1 - i % 2][j], memo[i % 2][j + 1])

        return memo[m % 2][n]

# Time: O(MN)
# Space:O(Min(M,N))


